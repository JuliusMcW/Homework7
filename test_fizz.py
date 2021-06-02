import unittest
import fizz


class Tester(unittest.TestCase):
    def test_fizz1(self):
        result = fizz.buzz(15)
        self.assertEqual(result,"Print 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ")
   