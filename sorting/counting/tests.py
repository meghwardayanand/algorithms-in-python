import unittest

from sorting.counting.countingSort import CountingSort


class TestCountingSort(unittest.TestCase):

    def setUp(self):
        self.unsorted_data = [4, 1, 3, 4, 3]
        self.sorted_data = [1, 3, 3, 4, 4]
        self.empty_data = []
        self.single_element_data = [42]
        self.duplicate_elements_data = [5, 1, 4, 2, 2, 3]

    def test_sort_unsorted_data(self):
        countingSort = CountingSort(self.unsorted_data)
        self.assertEqual(countingSort.sort(), self.sorted_data)

    def test_sort_empty_data(self):
        countingSort = CountingSort(self.empty_data)
        self.assertEqual(countingSort.sort(), self.empty_data)

    def test_sort_single_element_data(self):
        countingSort = CountingSort(self.single_element_data)
        self.assertEqual(countingSort.sort(), self.single_element_data)

    def test_sort_sorted_data(self):
        countingSort = CountingSort(self.sorted_data)
        self.assertEqual(countingSort.sort(), self.sorted_data)

    def test_sort_duplicate_data(self):
        countingSort = CountingSort(self.duplicate_elements_data)
        self.assertEqual(countingSort.sort(), [1, 2, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
