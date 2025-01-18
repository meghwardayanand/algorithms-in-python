import unittest

from applications.stack.reverseString.reverseString import String


class TestString(unittest.TestCase):

    def test_reverse_simple(self):
        self.assertEqual(String("hello").reverse(), "olleh")

    def test_reverse_single_character(self):
        self.assertEqual(String("a").reverse(), "a")

    def test_reverse_empty_string(self):
        self.assertEqual(String("").reverse(), "")

    def test_reverse_palindrome(self):
        self.assertEqual(String("madam").reverse(), "madam")

    def test_reverse_multiple_spaces(self):
        self.assertEqual(String("a b c").reverse(), "c b a")

    def test_reverse_with_special_characters(self):
        self.assertEqual(String("hello!@#").reverse(), "#@!olleh")

    def test_reverse_numbers_in_string(self):
        self.assertEqual(String("12345").reverse(), "54321")

    def test_reverse_with_mixed_case(self):
        self.assertEqual(String("HeLLo").reverse(), "oLLeH")

    def test_reverse_large_string(self):
        self.assertEqual(String("a" * 1000).reverse(), "a" * 1000)

    def test_reverse_large_input_with_special_chars(self):
        self.assertEqual(String("a!b@c#d$e%f^g&h*i(j)k").reverse(), "k)j(i*h&g^f%e$d#c@b!a")


if __name__ == "__main__":
    unittest.main()
