from basic.stack.stack import Stack


class Parenthesis:
    def __init__(self, parenthesis: str):
        self.parenthesis = parenthesis
        self.length = len(parenthesis)
        self.stack = Stack(self.length, dtypes=[str])
        self.opening_parentheses = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

    def isValid(self):
        is_balanced = True
        index = 0
        while index < self.length and is_balanced:
            parenthesis = self.parenthesis[index]
            if parenthesis in "({[":
                self.stack.push(parenthesis)
            elif parenthesis in ")}]":
                if self.stack.isEmpty():
                    is_balanced = False
                else:
                    if self.stack.peek() != self.opening_parentheses.get(parenthesis):
                        is_balanced = False
                    else:
                        self.stack.pop()

            index += 1

        if not self.stack.isEmpty():
            is_balanced = False

        return is_balanced
