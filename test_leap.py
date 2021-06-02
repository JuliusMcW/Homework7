import unittest
import leap


class Tester(unittest.TestCase):
    def test_leap1(self):
        result = leap.leapy(1978)
        self.assertEqual(result,False)
