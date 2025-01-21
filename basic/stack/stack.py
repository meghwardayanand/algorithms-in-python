
class Stack:

    def __init__(self, size, is_limited=False, dtypes=[int]):
        self.size = size
        self.data = []
        self.is_limited = is_limited
        self.dtypes = dtypes

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return len(self.data) == self.size if self.is_limited else False

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty, cannot pop more items.")

        item = self.data[-1]        # extract item
        del self.data[-1]           # remove it from stack
        return item                 # return the item

    def push(self, item):
        if not any([isinstance(item, dtype) for dtype in self.dtypes]):
            raise Exception(f"Invalid data type for the item to push on stack.")
        
        if self.isFull():
            raise Exception(f"Stack is already full with {self.size} items, cannot push more items.")

        self.data.append(item)
        if not self.is_limited and len(self.data) == self.size:
            self.size += 1

    def peek(self):
        return None if self.isEmpty() else self.data[-1]
