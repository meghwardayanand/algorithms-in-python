import unittest
from basic.stack.stack import Stack


class StackTest(unittest.TestCase):

    def setUp(self):
        self.stack_unlimited = Stack(size=5, isLimited=False, dtypes=[int])
        self.stack_limited = Stack(size=3, isLimited=True, dtypes=[int, str])

    def test_is_empty(self):
        self.assertTrue(self.stack_limited.isEmpty())
        self.assertTrue(self.stack_unlimited.isEmpty())

    def test_push(self):
        self.stack_unlimited.push(10)
        self.assertEqual(self.stack_unlimited.peek(), 10)

        self.stack_limited.push("hello")
        self.assertEqual(self.stack_limited.peek(), "hello")

    def test_push_invalid_type(self):
        self.assertRaises(Exception, self.stack_limited.push, {})
        self.assertRaises(Exception, self.stack_unlimited.push, "hello")

    def test_is_full(self):
        self.stack_limited.push("hi")
        self.stack_limited.push("world")
        self.stack_limited.push("hello world")
        self.assertRaises(Exception, self.stack_limited.push, "hello world again")
        self.assertTrue(self.stack_limited.isFull())
        self.assertFalse(self.stack_unlimited.isFull())

    def test_pop_when_empty(self):
        self.assertRaises(Exception, self.stack_limited.pop)
        self.assertRaises(Exception, self.stack_unlimited.pop)

    def test_pop(self):
        self.stack_limited.push("hello world")
        self.stack_unlimited.push(23)
        self.assertEqual(self.stack_limited.pop(), "hello world")
        self.assertEqual(self.stack_unlimited.pop(), 23)
        self.assertTrue(self.stack_limited.isEmpty())
        self.assertTrue(self.stack_unlimited.isEmpty())

    def test_peek_when_empty(self):
        self.assertIsNone(self.stack_limited.peek())
        self.assertIsNone(self.stack_unlimited.peek())

    def test_peek(self):
        self.stack_limited.push("hello world")
        self.stack_unlimited.push(23)
        self.assertEqual(self.stack_limited.peek(), "hello world")
        self.assertEqual(self.stack_unlimited.peek(), 23)

        self.stack_limited.push("monster")
        self.stack_unlimited.push(789)
        self.assertEqual(self.stack_limited.peek(), "monster")
        self.assertEqual(self.stack_unlimited.peek(), 789)


if __name__ == "__main__":
    unittest.main()
