from basic.stack.stack import Stack


class String:
    def __init__(self, string):
        self.string = string
        self.length = len(string)
        self.stack = Stack(self.length, dtypes=[str])

    def reverse(self):
        for char in self.string:
            self.stack.push(char)

        return "".join([self.stack.pop() for _ in range(self.length)])
