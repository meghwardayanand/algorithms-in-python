import unittest

from basic.linkedList.doubleEnded.doubleEndedLinkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_at_front(self):
        self.linked_list.insertAtFront(-134)
        self.linked_list.insertAtFront(244)
        self.linked_list.insertAtFront(103423)

        expected = "103423 <--> 244 <--> -134"
        self.assertEqual(repr(self.linked_list), expected)

    def test_insert_at_end(self):
        self.linked_list.insertAtEnd(-134)
        self.linked_list.insertAtEnd(244)
        self.linked_list.insertAtEnd(103423)

        expected = "-134 <--> 244 <--> 103423"
        self.assertEqual(repr(self.linked_list), expected)

    def test_remove_from_front(self):
        self.linked_list.insertAtEnd(-134)
        self.linked_list.insertAtEnd(244)
        self.linked_list.insertAtEnd(103423)

        self.linked_list.removeFromFront()
        expected = "244 <--> 103423"
        self.assertEqual(repr(self.linked_list), expected)

    def test_remove_from_end(self):
        self.linked_list.insertAtEnd(-134)
        self.linked_list.insertAtEnd(244)
        self.linked_list.insertAtEnd(103423)

        self.linked_list.removeFromEnd()
        expected = "-134 <--> 244"
        self.assertEqual(repr(self.linked_list), expected)

    def test_is_found_true(self):
        self.linked_list.insertAtEnd(-134)
        self.linked_list.insertAtEnd(244)
        self.linked_list.insertAtEnd(103423)

        self.assertTrue(self.linked_list.isFound(244))
        self.assertTrue(self.linked_list.isFound(-134))
        self.assertTrue(self.linked_list.isFound(103423))

    def test_is_found_false(self):
        self.linked_list.insertAtEnd(-134)
        self.linked_list.insertAtEnd(244)
        self.linked_list.insertAtEnd(103423)

        self.assertFalse(self.linked_list.isFound(-100))
        self.assertFalse(self.linked_list.isFound(0))
        self.assertFalse(self.linked_list.isFound(1000))

    def test_find_existing_node(self):
        self.linked_list.insertAtEnd(-134)
        self.linked_list.insertAtEnd(244)
        self.linked_list.insertAtEnd(103423)

        node = self.linked_list.find(244)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 244)

        node = self.linked_list.find(-134)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, -134)

        node = self.linked_list.find(103423)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 103423)

    def test_find_non_existing_node(self):
        self.linked_list.insertAtEnd(-134)
        self.linked_list.insertAtEnd(244)
        self.linked_list.insertAtEnd(103423)

        node = self.linked_list.find(-135)
        self.assertIsNone(node)

        node = self.linked_list.find(245)
        self.assertIsNone(node)

        node = self.linked_list.find(103424)
        self.assertIsNone(node)

    def test_delete_from_front_empty_list(self):
        result = self.linked_list.removeFromFront()
        self.assertFalse(result)
        self.assertEqual(repr(self.linked_list), "Empty Double Ended LinkedList!")

    def test_delete_from_end_empty_list(self):
        result = self.linked_list.removeFromEnd()
        self.assertFalse(result)
        self.assertEqual(repr(self.linked_list), "Empty Double Ended LinkedList!")

    def test_repr_method(self):
        self.linked_list.insertAtEnd(-134)
        self.linked_list.insertAtEnd(244)
        self.linked_list.insertAtEnd(103423)

        expected = "-134 <--> 244 <--> 103423"
        self.assertEqual(repr(self.linked_list), expected)

    def test_multiple_operations(self):
        self.linked_list.insertAtEnd(-10)
        self.linked_list.insertAtEnd(20)
        self.linked_list.insertAtFront(-5)
        self.linked_list.insertAtEnd(30)

        expected = "-5 <--> -10 <--> 20 <--> 30"
        self.assertEqual(repr(self.linked_list), expected)

        self.linked_list.removeFromFront()
        expected_after_deletion = "-10 <--> 20 <--> 30"
        self.assertEqual(repr(self.linked_list), expected_after_deletion)

        self.linked_list.removeFromEnd()
        expected_after_deletion_end = "-10 <--> 20"
        self.assertEqual(repr(self.linked_list), expected_after_deletion_end)

        self.assertTrue(self.linked_list.isFound(20))
        self.assertFalse(self.linked_list.isFound(40))

    def test_display_empty_list(self):
        self.assertEqual(repr(self.linked_list), "Empty Double Ended LinkedList!")


if __name__ == '__main__':
    unittest.main()
