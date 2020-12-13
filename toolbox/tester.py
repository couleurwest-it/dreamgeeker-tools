import unittest
from app import tools
from app.config import CConfig
from app.logmng import CTracker

CConfig('app')


class MyTestCase(unittest.TestCase):
    def testinit(self):
        print('Configuration')
        print(tools.string_me(55))
    def testlog(self):
        CTracker.info_tracking('test message info', 'je test')


if __name__ == '__main__':
    unittest.main()
