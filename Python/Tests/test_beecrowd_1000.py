
import sys
import os
sys.path.append(os.path.abspath('../Problems'))
#Creates a unified path for Problems and Tests

import unittest
import beecrowd_1000


class TestCalc(unittest.TestCase):

    # Checking Output
    def test_beginner1000(self):
        result = beecrowd_1000.beginner1000()
        self.assertEqual(result,"Hello World!")


if __name__ == '__main__':
    unittest.main()
