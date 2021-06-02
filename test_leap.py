import unittest
import leap.py


class Tester(unittest.TestCase):
    def test_leap1(self):
        result = Julius_McWilliams_hw1.leap(1978)
        self.assertEqual(result,False)
