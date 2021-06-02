import unittest
import leap


class Tester(unittest.TestCase):
    def test_leap1(self):
        result = leap.leapy(1978)
        self.assertEqual(result,False)
    def test_leap2(self):
        result = leap.leapy(2000)
        self.assertEqual(result,True)
    def test_leap3(self):
        result = leap.leapy(2100)
        self.assertEqual(result,False)
