import unittest
import fizz


class Tester(unittest.TestCase):
    def test_fizz1(self):
        result = fizz.buzz(15)
        self.assertEqual(result,"Print 1 2 fizz 4 5 fizz 7 8 fizz 10 11 fizz 13 14 fizz ")
