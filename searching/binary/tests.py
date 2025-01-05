import unittest

from searching.binary.binarySearch import BinarySearch


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.sorted_data = [11, 12, 22, 25, 34, 64, 90]
        self.empty_data = []
        self.single_element_data = [42]
        self.duplicate_elements_data = [1, 2, 2, 3, 4, 5]
        self.negative_numbers_data = [-3, -2, -1, 0, 5]
        self.large_data = list(range(1, 10**6 + 1))

    def test_search_empty_data(self):
        binarySearch = BinarySearch(self.empty_data)
        self.assertEqual(binarySearch.search(34), None)

    def test_search_single_element_data(self):
        binarySearch = BinarySearch(self.single_element_data)
        self.assertEqual(binarySearch.search(42), 42)
        self.assertEqual(binarySearch.search(424), None)

    def test_search_sorted_data(self):
        binarySearch = BinarySearch(self.sorted_data)
        self.assertEqual(binarySearch.search(25), 25)
        self.assertEqual(binarySearch.search(3883), None)
        self.assertEqual(binarySearch.search(11), 11)
        self.assertEqual(binarySearch.search(90), 90)

    def test_search_duplicate_data(self):
        binarySearch = BinarySearch(self.duplicate_elements_data)
        self.assertEqual(binarySearch.search(2), 2)
        self.assertEqual(binarySearch.search(3883), None)
        self.assertEqual(binarySearch.search(1), 1)
        self.assertEqual(binarySearch.search(5), 5)


    def test_search_negative_numbers(self):
        binarySearch = BinarySearch(self.negative_numbers_data)
        self.assertEqual(binarySearch.search(-1), -1)
        self.assertEqual(binarySearch.search(3883), None)
        self.assertEqual(binarySearch.search(-3), -3)
        self.assertEqual(binarySearch.search(5), 5)


    def test_search_large_data(self):
        binarySearch = BinarySearch(self.large_data)
        self.assertEqual(binarySearch.search((10**6)//2), (10**6)//2)
        self.assertEqual(binarySearch.search(-3883), None)
        self.assertEqual(binarySearch.search(1), 1)
        self.assertEqual(binarySearch.search(10**6), 10**6)

if __name__ == "__main__":
    unittest.main()
