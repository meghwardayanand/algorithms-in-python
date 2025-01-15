import unittest

from basic.linkedList.circular.circularLinkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_at_front(self):
        self.linked_list.insertAtFront(10)
        self.linked_list.insertAtFront(20)
        self.linked_list.insertAtFront(30)

        expected = "30 --> 20 --> 10 --> (head)"
        self.assertEqual(repr(self.linked_list), expected)

    def test_insert_at_end(self):
        self.linked_list.insertAtEnd(10)
        self.linked_list.insertAtEnd(20)
        self.linked_list.insertAtEnd(30)

        expected = "10 --> 20 --> 30 --> (head)"
        self.assertEqual(repr(self.linked_list), expected)

    def test_remove_from_front(self):
        self.linked_list.insertAtEnd(10)
        self.linked_list.insertAtEnd(20)
        self.linked_list.insertAtEnd(30)

        self.linked_list.removeFromFront()
        expected = "20 --> 30 --> (head)"
        self.assertEqual(repr(self.linked_list), expected)

    def test_remove_from_end(self):
        self.linked_list.insertAtEnd(10)
        self.linked_list.insertAtEnd(20)
        self.linked_list.insertAtEnd(30)

        self.linked_list.removeFromEnd()
        expected = "10 --> 20 --> (head)"
        self.assertEqual(repr(self.linked_list), expected)

    def test_remove_from_empty_list(self):
        self.assertFalse(self.linked_list.removeFromFront())
        self.assertEqual(repr(self.linked_list), "Empty Circular LinkedList!")

    def test_is_found_true(self):
        self.linked_list.insertAtEnd(10)
        self.linked_list.insertAtEnd(20)
        self.linked_list.insertAtEnd(30)

        self.assertTrue(self.linked_list.isFound(20))
        self.assertTrue(self.linked_list.isFound(30))
        self.assertTrue(self.linked_list.isFound(10))

    def test_is_found_false(self):
        self.linked_list.insertAtEnd(10)
        self.linked_list.insertAtEnd(20)
        self.linked_list.insertAtEnd(30)

        self.assertFalse(self.linked_list.isFound(-40))
        self.assertFalse(self.linked_list.isFound(50))

    def test_find_existing_node(self):
        self.linked_list.insertAtEnd(10)
        self.linked_list.insertAtEnd(20)
        self.linked_list.insertAtEnd(30)

        node = self.linked_list.find(20)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 20)

    def test_find_non_existing_node(self):
        self.linked_list.insertAtEnd(10)
        self.linked_list.insertAtEnd(20)
        self.linked_list.insertAtEnd(30)
        self.assertIsNone(self.linked_list.find(40))

    def test_repr_method(self):
        self.linked_list.insertAtEnd(10)
        self.linked_list.insertAtEnd(20)
        self.linked_list.insertAtEnd(30)

        expected = "10 --> 20 --> 30 --> (head)"
        self.assertEqual(repr(self.linked_list), expected)

    def test_single_node_list(self):
        self.linked_list.insertAtEnd(10)
        self.assertEqual(repr(self.linked_list), "10 --> (head)")
        self.assertTrue(self.linked_list.removeFromFront())
        self.assertEqual(repr(self.linked_list), "Empty Circular LinkedList!")

if __name__ == '__main__':
    unittest.main()
