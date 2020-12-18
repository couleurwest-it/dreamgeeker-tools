import unittest

from toolbox import tools
from toolbox.config import CConfig
from toolbox.logmng import CTracker

CConfig('toolbox')


class MyTestCase(unittest.TestCase):
    def testinit(self):
        print('Configuration')
        print(tools.string_me(55))
    def testlog(self):
        CTracker.info_tracking('test message info', 'je test')


if __name__ == '__main__':
    unittest.main()
