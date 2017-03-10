import unittest

from all_your_base import *


class AllYourBaseTests(unittest.TestCase):

    @unittest.skip('skip')
    def test_foldl_string(self):
        add = lambda x1, x2: x1 + x2
        string = 'Hello, foldl!'
        charlist = [c for c in string]
        self.assertEqual(string, foldl(add, charlist, ''))

    @unittest.skip('skip')
    def test_foldl_list_of_numbers(self):
        add = lambda x1, x2: x1 + x2
        dgts = range(10)
        self.assertEqual(sum(dgts), foldl(add, dgts, 0))

    def test_to_base10(self):
        self.assertEqual(5, to_base10(2, [1, 0, 1]))
        self.assertEqual(36, to_base10(3, [1, 1, 0, 0]))

    def test_fr_base10(self):
        base = 3
        dgts = [1, 1, 0, 1, 0]
        self.assertEqual(dgts, fr_base10(base, to_base10(base, dgts)))

    #@unittest.skip('skip')
    def test_single_bit_to_one_decimal(self):
        self.assertEqual(rebase(2, [1], 10), [1])

    #@unittest.skip('skip')
    def test_binary_to_single_decimal(self):
        self.assertEqual(rebase(2, [1, 0, 1], 10), [5])

    #@unittest.skip('skip')
    def test_single_decimal_to_binary(self):
        self.assertEqual(rebase(10, [5], 2), [1, 0, 1])

    #@unittest.skip('skip')
    def test_binary_to_multiple_decimal(self):
        self.assertEqual(rebase(2, [1, 0, 1, 0, 1, 0], 10), [4, 2])

    #@unittest.skip('skip')
    def test_decimal_to_binary(self):
        self.assertEqual(rebase(10, [4, 2], 2), [1, 0, 1, 0, 1, 0])

    #@unittest.skip('skip')
    def test_trinary_to_hexadecimal(self):
        self.assertEqual(rebase(3, [1, 1, 2, 0], 16), [2, 10])

    #@unittest.skip('skip')
    def test_hexadecimal_to_trinary(self):
        self.assertEqual(rebase(16, [2, 10], 3), [1, 1, 2, 0])

    #@unittest.skip('skip')
    def test_15_bit_integer(self):
        self.assertEqual(rebase(97, [3, 46, 60], 73), [6, 10, 45])

    #@unittest.skip('skip')
    def test_empty_list(self):
        self.assertEqual(rebase(2, [], 10), [])

    #@unittest.skip('skip')
    def test_single_zero(self):
        self.assertEqual(rebase(10, [0], 2), [])

    #@unittest.skip('skip')
    def test_multiple_zeroes(self):
        self.assertEqual(rebase(10, [0, 0, 0], 2), [])

    #@unittest.skip('skip')
    def test_leading_zeros(self):
        self.assertEqual(rebase(7, [0, 6, 0], 10), [4, 2])

    def test_negative_digit(self):
        with self.assertRaises(ValueError):
            rebase(2, [1, -1, 1, 0, 1, 0], 10)

    def test_invalid_positive_digit(self):
        with self.assertRaises(ValueError):
            rebase(2, [1, 2, 1, 0, 1, 0], 10)

    def test_first_base_is_one(self):
        with self.assertRaises(ValueError):
            rebase(1, [], 10)

    def test_second_base_is_one(self):
        with self.assertRaises(ValueError):
            rebase(2, [1, 0, 1, 0, 1, 0], 1)

    def test_first_base_is_zero(self):
        with self.assertRaises(ValueError):
            rebase(0, [], 10)

    def test_second_base_is_zero(self):
        with self.assertRaises(ValueError):
            rebase(10, [7], 0)

    def test_first_base_is_negative(self):
        with self.assertRaises(ValueError):
            rebase(-2, [1], 10)

    def test_second_base_is_negative(self):
        with self.assertRaises(ValueError):
            rebase(2, [1], -7)

    def test_both_bases_are_negative(self):
        with self.assertRaises(ValueError):
            rebase(-2, [1], -7)


if __name__ == '__main__':
    unittest.main()
