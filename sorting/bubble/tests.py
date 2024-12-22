import unittest
from sorting.bubble.bubbleSort import BubbleSort


class StackTest(unittest.TestCase):

    def setUp(self):
        self.unsorted_data = [64, 34, 25, 12, 22, 11, 90]
        self.sorted_data = [11, 12, 22, 25, 34, 64, 90]
        self.empty_data = []
        self.single_element_data = [42]
        self.duplicate_elements_data = [5, 1, 4, 2, 2, 3]
        self.negative_numbers_data = [-1, -3, -2, 5, 0]

    def test_sort_unsorted_data(self):
        bubbleSort = BubbleSort(self.unsorted_data)
        self.assertEqual(bubbleSort.sort(), self.sorted_data)

    def test_sort_empty_data(self):
        bubbleSort = BubbleSort(self.empty_data)
        self.assertEqual(bubbleSort.sort(), self.empty_data)

    def test_sort_single_element_data(self):
        bubbleSort = BubbleSort(self.single_element_data)
        self.assertEqual(bubbleSort.sort(), self.single_element_data)

    def test_sort_sorted_data(self):
        bubbleSort = BubbleSort(self.sorted_data)
        self.assertEqual(bubbleSort.sort(), self.sorted_data)

    def test_sort_duplicate_data(self):
        bubbleSort = BubbleSort(self.duplicate_elements_data)
        self.assertEqual(bubbleSort.sort(), [1, 2, 2, 3, 4, 5])

    def test_sort_negative_numbers(self):
        bubbleSort = BubbleSort(self.negative_numbers_data)
        self.assertEqual(bubbleSort.sort(), [-3, -2, -1, 0, 5])


if __name__ == "__main__":
    unittest.main()
