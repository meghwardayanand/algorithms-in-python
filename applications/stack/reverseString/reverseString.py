from basic.stack.stack import Stack


class String:
    def __init__(self, string):
        self.string = string
        self.length = len(string)
        self.stack = Stack(self.length, dtypes=[str])
        self.specials = "@_!#$%^&*()<>?/\|}{~:, "

    def reverse(self, ignore_specials=False):
        for char in self.string:
            if ignore_specials and char in self.specials:
                continue

            self.stack.push(char)

        return "".join([self.stack.pop() for _ in range(self.length) if not self.stack.isEmpty()])

    def isPalindrome(self):
        actual_string = "".join([char.lower() for char in self.string if char not in self.specials])
        return actual_string == self.reverse(ignore_specials=True).lower()
