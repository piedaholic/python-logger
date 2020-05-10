import unittest
from logger import Logger

class Test(unittest.TestCase):

    def test_debug_file(self):
        #filename = 'D:\\Temp\\MyLogs\\USER1.log'
        filename = 'USER1'
        message = 'Hello World!'
        logger = Logger(debug_path='D:\\Temp\\MyLogs\\', filename=None)
        #logger = Logger(debug_path='D:\\Temp\\MyLogs\\',filename=filename)
        logger.debug(message)
        logger.info(message)
        #logger.flush()

if __name__ == '__main__':
    unittest.main()
