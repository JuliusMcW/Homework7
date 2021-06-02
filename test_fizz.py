import unittest
import fizz


class Tester(unittest.TestCase):
    def test_fizz2(self):
        result = fizz.buzz(15)
        self.assertEqual(result,"Print 1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz ")
