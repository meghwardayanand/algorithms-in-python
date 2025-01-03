import unittest

from sorting.heap.heap.heapSortAscending import HeapSortAscending
from sorting.heap.heap.heapSortDescending import HeapSortDescending


class TestHeapSort(unittest.TestCase):

    def setUp(self):
        self.unsorted_data = [64, 34, 25, 12, 22, 11, 90]
        self.sorted_data = [11, 12, 22, 25, 34, 64, 90]
        self.sorted_data_descending = [90, 64, 34, 25, 22, 12, 11]
        self.empty_data = []
        self.single_element_data = [42]
        self.duplicate_elements_data = [5, 1, 4, 2, 2, 3]
        self.negative_numbers_data = [-1, -3, -2, 5, 0]

    def test_ascending_sort_unsorted_data(self):
        heapSortAscending = HeapSortAscending(self.unsorted_data)
        self.assertEqual(heapSortAscending.sort(), self.sorted_data)

    def test_ascending_sort_empty_data(self):
        heapSortAscendingAscending = HeapSortAscending(self.empty_data)
        self.assertEqual(heapSortAscendingAscending.sort(), self.empty_data)

    def test_ascending_sort_single_element_data(self):
        heapSortAscending = HeapSortAscending(self.single_element_data)
        self.assertEqual(heapSortAscending.sort(), self.single_element_data)

    def test_ascending_sort_sorted_data(self):
        heapSortAscending = HeapSortAscending(self.sorted_data)
        self.assertEqual(heapSortAscending.sort(), self.sorted_data)

    def test_ascending_sort_duplicate_data(self):
        heapSortAscending = HeapSortAscending(self.duplicate_elements_data)
        self.assertEqual(heapSortAscending.sort(), [1, 2, 2, 3, 4, 5])

    def test_ascending_sort_negative_numbers(self):
        heapSortAscending = HeapSortAscending(self.negative_numbers_data)
        self.assertEqual(heapSortAscending.sort(), [-3, -2, -1, 0, 5])

    def test_descending_sort_unsorted_data(self):
        heapSortDescending = HeapSortDescending(self.unsorted_data)
        self.assertEqual(heapSortDescending.sort(), self.sorted_data_descending)

    def test_descending_sort_empty_data(self):
        heapSortDescendingAscending = HeapSortDescending(self.empty_data)
        self.assertEqual(heapSortDescendingAscending.sort(), self.empty_data)

    def test_descending_sort_single_element_data(self):
        heapSortDescending = HeapSortDescending(self.single_element_data)
        self.assertEqual(heapSortDescending.sort(), self.single_element_data)

    def test_descending_sort_sorted_data(self):
        heapSortDescending = HeapSortDescending(self.sorted_data_descending)
        self.assertEqual(heapSortDescending.sort(), self.sorted_data_descending)

    def test_descending_sort_duplicate_data(self):
        heapSortDescending = HeapSortDescending(self.duplicate_elements_data)
        self.assertEqual(heapSortDescending.sort(), [5, 4, 3, 2, 2, 1])

    def test_descending_sort_negative_numbers(self):
        heapSortDescending = HeapSortDescending(self.negative_numbers_data)
        self.assertEqual(heapSortDescending.sort(), [5, 0, -1, -2, -3])


if __name__ == "__main__":
    unittest.main()
