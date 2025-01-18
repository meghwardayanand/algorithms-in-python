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

    def test_is_palindrome_simple(self):
        self.assertTrue(String("madam").isPalindrome())

    def test_is_palindrome_single_character(self):
        self.assertTrue(String("a").isPalindrome())

    def test_is_palindrome_empty_string(self):
        self.assertTrue(String("").isPalindrome())

    def test_is_not_palindrome(self):
        self.assertFalse(String("hello").isPalindrome())

    def test_is_palindrome_even_length(self):
        self.assertTrue(String("abba").isPalindrome())

    def test_is_not_palindrome_even_length(self):
        self.assertFalse(String("abca").isPalindrome())

    def test_is_palindrome_with_spaces(self):
        self.assertTrue(String("a man a plan a canal panama").isPalindrome())

    def test_is_palindrome_with_special_characters(self):
        self.assertTrue(String("A man, a plan, a canal, Panama!").isPalindrome())

    def test_is_not_palindrome_with_special_characters(self):
        self.assertFalse(String("hello, world!").isPalindrome())

    def test_is_palindrome_mixed_case(self):
        self.assertTrue(String("RaceCar").isPalindrome())

    def test_is_palindrome_with_numbers(self):
        self.assertTrue(String("12321").isPalindrome())

    def test_is_palindrome_with_mixed_content(self):
        self.assertTrue(String("A car, a man, a maraca!").isPalindrome())

    def test_is_not_palindrome_with_mixed_content(self):
        self.assertFalse(String("No 'x' in Nixon").isPalindrome())

    def test_is_palindrome_with_long_string(self):
        self.assertTrue(String("a" * 1000 + "b" + "a" * 1000).isPalindrome())    


if __name__ == "__main__":
    unittest.main()
