import unittest

from searching.sequential.sequentialSearch import SequentialSearch


class TestSequentialSearch(unittest.TestCase):

    def setUp(self):
        self.unsorted_data = [64, 34, 25, 12, 22, 11, 90]
        self.sorted_data = [11, 12, 22, 25, 34, 64, 90]
        self.empty_data = []
        self.single_element_data = [42]
        self.duplicate_elements_data = [5, 1, 4, 2, 2, 3]
        self.negative_numbers_data = [-1, -3, -2, 5, 0]

    def test_search_unsorted_data(self):
        sequentialSearch = SequentialSearch(self.unsorted_data)
        self.assertEqual(sequentialSearch.search(12), 12)
        self.assertEqual(sequentialSearch.search(3883), None)
        self.assertEqual(sequentialSearch.search(64), 64)
        self.assertEqual(sequentialSearch.search(90), 90)

    def test_search_empty_data(self):
        sequentialSearch = SequentialSearch(self.empty_data)
        self.assertEqual(sequentialSearch.search(34), None)

    def test_search_single_element_data(self):
        sequentialSearch = SequentialSearch(self.single_element_data)
        self.assertEqual(sequentialSearch.search(42), 42)
        self.assertEqual(sequentialSearch.search(424), None)

    def test_search_sorted_data(self):
        sequentialSearch = SequentialSearch(self.sorted_data)
        self.assertEqual(sequentialSearch.search(25), 25)
        self.assertEqual(sequentialSearch.search(3883), None)
        self.assertEqual(sequentialSearch.search(11), 11)
        self.assertEqual(sequentialSearch.search(90), 90)

    def test_search_duplicate_data(self):
        sequentialSearch = SequentialSearch(self.duplicate_elements_data)
        self.assertEqual(sequentialSearch.search(2), 2)
        self.assertEqual(sequentialSearch.search(3883), None)
        self.assertEqual(sequentialSearch.search(1), 1)
        self.assertEqual(sequentialSearch.search(5), 5)


    def test_search_negative_numbers(self):
        sequentialSearch = SequentialSearch(self.negative_numbers_data)
        self.assertEqual(sequentialSearch.search(-1), -1)
        self.assertEqual(sequentialSearch.search(3883), None)
        self.assertEqual(sequentialSearch.search(-3), -3)
        self.assertEqual(sequentialSearch.search(5), 5)


if __name__ == "__main__":
    unittest.main()
