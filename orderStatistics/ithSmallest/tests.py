import unittest
import random

from orderStatistics.ithSmallest.ithSmallestNumber import IthSmallestNumber


class TestIthSmallestNumber(unittest.TestCase):

    def setUp(self):
        self.data = [7, 10, 4, 3, 20, 15]
        self.single_element = [42]
        self.duplicate_elements = [4, 2, 2, 5, 3, 4]
        self.negative_numbers = [-1, -3, -2, 5, 0]
        self.large_data = [random.randint(1, 1000000) for _ in range(10000)]

    def test_find_ith_smallest(self):
        ith_smallest = IthSmallestNumber(self.data)
        self.assertEqual(ith_smallest.findIthNumber(3), 7)

    def test_find_ith_smallest_single_element(self):
        ith_smallest = IthSmallestNumber(self.single_element)
        self.assertEqual(ith_smallest.findIthNumber(1), 42)

    def test_find_ith_smallest_duplicates(self):
        ith_smallest = IthSmallestNumber(self.duplicate_elements)
        self.assertEqual(ith_smallest.findIthNumber(3), 3)

    def test_find_ith_smallest_negative_numbers(self):
        ith_smallest = IthSmallestNumber(self.negative_numbers)
        self.assertEqual(ith_smallest.findIthNumber(2), -2)

    def test_find_ith_smallest_huge_array(self):
        ith_smallest = IthSmallestNumber(self.large_data)
        sorted_large_data = sorted(self.large_data)
        self.assertEqual(ith_smallest.findIthNumber(5000), sorted_large_data[4999])

    def test_lower_out_of_bounds(self):
        ith_smallest = IthSmallestNumber(self.data)
        with self.assertRaises(IndexError):
            ith_smallest.findIthNumber(0)

    def test_upper_out_of_bounds(self):
        ith_smallest = IthSmallestNumber(self.data)
        with self.assertRaises(IndexError):
            ith_smallest.findIthNumber(len(self.data) + 1)


if __name__ == "__main__":
    unittest.main()
