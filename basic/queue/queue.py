
class Queue:
    def __init__(self, size):
        self.arr = []
        self.size = size

    def enqueue(self, x):
        if self.is_full():
            raise IndexError("Queue is full!")

        self.arr.append(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")

        return self.arr.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")

        return self.arr[0]

    def is_empty(self):
        return len(self.arr) == 0

    def is_full(self):
        return self.size == len(self.arr)
