
class Queue:
    def __init__(self, size):
        self.arr = []
        self.size = size

    def enqueue(self, x):
        if self.isFull():
            raise IndexError("Queue is full!")

        self.arr.append(x)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty!")

        return self.arr.pop(0)

    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty!")

        return self.arr[0]

    def isEmpty(self):
        return len(self.arr) == 0

    def isFull(self):
        return self.size == len(self.arr)
