import logging
import os
from os.path import isfile, join

class Logger:

    logger_prop = dict()
    debug_path = str()
    debug_file_ext = str()

    def __init__(self, *args, **kwargs):
        if not bool(Logger.logger_prop):
            Logger.logger_prop = self.read_properties_file('logger.properties')
            if not bool(Logger.logger_prop):
                print('Failed to load logger.properties')
            Logger.debug_path = Logger.logger_prop['logger.debug.path']
            Logger.debug_file_ext = Logger.logger_prop['logger.debug.file.extension']
        if kwargs.get('filename') is None or kwargs.get('filename') == '':
            kwargs['filename'] = 'Client'
        if kwargs.get('debug_path') is None:
            self.load_default_out_dir(kwargs.get('filename'))
        else:
            self.load_custom_out_dir(kwargs.get('debug_path'),kwargs.get('filename'))

    def load_default_out_dir(self,filename):
            self.logger = logging.getLogger(filename)
            self.logger.info('Logger created for '+ filename)
            self.logger.setLevel(logging.DEBUG)
            file = os.path.join(Logger.debug_path , filename + Logger.debug_file_ext)

            # create file handler which logs even debug messages
            fh = logging.FileHandler(file)
            fh.setLevel(logging.DEBUG)

            # create console handler with a higher log level
            ch = logging.StreamHandler()
            ch.setLevel(logging.ERROR)
            formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s]%(message)s')
            ch.setFormatter(formatter)
            fh.setFormatter(formatter)
            # add the handlers to logger
            self.logger.addHandler(ch)
            self.logger.addHandler(fh)

    def load_custom_out_dir(self, debug_directory, filename):
            if debug_directory is None:
                debug_directory = Logger.debug_path

            self.logger = logging.getLogger(filename)
            self.logger.info('Logger created for '+ filename)
            self.logger.setLevel(logging.DEBUG)

            file = os.path.join(debug_directory , filename + Logger.debug_file_ext)
            print(file)
            # create file handler which logs even debug messages
            fh = logging.FileHandler(file)
            fh.setLevel(logging.DEBUG)

            # create console handler with a higher log level
            ch = logging.StreamHandler()
            ch.setLevel(logging.ERROR)
            formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s]%(message)s')
            ch.setFormatter(formatter)
            fh.setFormatter(formatter)
            # add the handlers to logger
            self.logger.addHandler(ch)
            self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message);

    def info(self, message):
        self.logger.info(message);

    def flush(self):
        self.logger.handlers[0].flush()
        self.logger.handlers[1].flush()

    def read_properties_file(self, path):
        prop_file = open(path, "r")
        prop_dict = dict()
        for prop_line in prop_file:
            prop_def = prop_line.strip()
            if len(prop_def) == 0:
                continue
            if prop_def[0] in ('!', '#'):
                continue
            punctuation = [prop_def.find(c) for c in '='] + [len(prop_def)]
            found = min([pos for pos in punctuation if pos != -1])
            name = prop_def[:found].rstrip()
            value = prop_def[found:].lstrip("=").rstrip()
            prop_dict[name] = value
        prop_file.close()
        # print propDict
        return prop_dict
