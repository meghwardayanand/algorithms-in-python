import unittest

from basic.queue.queue import Queue


class TestQueue(unittest.TestCase):

    def test_empty_queue(self):
        queue = Queue(size=0)
        self.assertTrue(queue.isEmpty())
        self.assertTrue(queue.isFull())
        self.assertRaises(IndexError, queue.peek)
        self.assertRaises(IndexError, queue.enqueue, 23)
        self.assertRaises(IndexError, queue.dequeue)

    def test_enqueue_and_dequeue(self):
        queue = Queue(3)
        self.assertTrue(queue.isEmpty())
        self.assertFalse(queue.isFull())
        self.assertRaises(IndexError, queue.peek)

        queue.enqueue(10)
        self.assertFalse(queue.isEmpty())
        self.assertFalse(queue.isFull())
        self.assertEqual(queue.peek(), 10)

        queue.enqueue(20)
        self.assertFalse(queue.isEmpty())
        self.assertFalse(queue.isFull())
        self.assertEqual(queue.peek(), 10)

        queue.enqueue(30)
        self.assertFalse(queue.isEmpty())
        self.assertTrue(queue.isFull())
        self.assertEqual(queue.peek(), 10)

        queue.dequeue()
        self.assertFalse(queue.isEmpty())
        self.assertFalse(queue.isFull())
        self.assertEqual(queue.peek(), 20)

        queue.dequeue()
        self.assertFalse(queue.isEmpty())
        self.assertFalse(queue.isFull())
        self.assertEqual(queue.peek(), 30)

        queue.dequeue()
        self.assertTrue(queue.isEmpty())
        self.assertFalse(queue.isFull())
        self.assertRaises(IndexError, queue.peek)

    def test_queue_is_full(self):
        queue = Queue(size=2)
        queue.enqueue(1)
        self.assertFalse(queue.isFull())
        queue.enqueue(2)
        self.assertTrue(queue.isFull())
        queue.dequeue()
        self.assertFalse(queue.isFull())

    def test_queue_is_empty(self):
        queue = Queue(size=2)
        self.assertTrue(queue.isEmpty())
        queue.enqueue(1)
        self.assertFalse(queue.isEmpty())
        queue.dequeue()
        self.assertTrue(queue.isEmpty())

    def test_queue_peek(self):
        queue = Queue(size=2)
        self.assertRaises(IndexError, queue.peek)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 1)
        queue.dequeue()
        self.assertEqual(queue.peek(), 2)
        queue.dequeue()
        self.assertRaises(IndexError, queue.peek)


if __name__ == '__main__':
    unittest.main()
