import unittest

from applications.stack.validParentheses.validParentheses import Parenthesis


class TestStack(unittest.TestCase):

    def test_empty_str(self):
        self.assertTrue(Parenthesis("").isValid())

    def test_valid_simple(self):
        self.assertTrue(Parenthesis("()").isValid())

    def test_valid_with_diff_types(self):
        self.assertTrue(Parenthesis("{[()()]}").isValid())

    def test_invalid_mismatched(self):
        self.assertFalse(Parenthesis("([)]").isValid())

    def test_valid_nested(self):
        self.assertTrue(Parenthesis("((()))").isValid())

    def test_invalid_extra_closing(self):
        self.assertFalse(Parenthesis("(()))").isValid())

    def test_single_open_parenthesis(self):
        self.assertFalse(Parenthesis("(").isValid())

    def test_single_close_parenthesis(self):
        self.assertFalse(Parenthesis(")").isValid())

    def test_valid_with_multiple_types(self):
        self.assertTrue(Parenthesis("[{()}]").isValid())

    def test_only_open_parentheses(self):
        self.assertFalse(Parenthesis("((({{{").isValid())

    def test_only_close_parentheses(self):
        self.assertFalse(Parenthesis(")}})").isValid())

    def test_large_valid(self):
        self.assertTrue(Parenthesis("({[({[()]})]})").isValid())

    def test_large_invalid(self):
        self.assertFalse(Parenthesis("({[({[())]})]})").isValid())

    def test_no_pairs(self):
        self.assertTrue(Parenthesis("{}[]()").isValid())

    def test_with_whitespace_and_other_chars(self):
        self.assertTrue(Parenthesis("([ ] { } ( ) )").isValid())

    def test_complex_mismatched(self):
        self.assertFalse(Parenthesis("([)]{(})").isValid())

    def test_long_balanced(self):
        self.assertTrue(Parenthesis("(()()())(())(()()())").isValid())

    def test_long_unbalanced(self):
        self.assertFalse(Parenthesis("(()()())(())(()()()").isValid())

    def test_valid_with_multiple_types_and_nesting(self):
        self.assertTrue(Parenthesis("({[]()})").isValid())

    def test_multiple_valid_parentheses(self):
        self.assertTrue(Parenthesis("({[()]}{[()()]})").isValid())

    def test_one_char_strings(self):
        self.assertTrue(Parenthesis("4").isValid())
        self.assertFalse(Parenthesis("(").isValid())
        self.assertFalse(Parenthesis(")").isValid())

    def test_random_valid_str(self):
        self.assertTrue(Parenthesis("(())").isValid())
        self.assertTrue(Parenthesis("[({})]").isValid())
        self.assertTrue(Parenthesis("{}[]()").isValid())
        self.assertTrue(Parenthesis("{[][]{[]()}()}").isValid())

    def test_random_invalid_str(self):
        self.assertFalse(Parenthesis("({[)}").isValid())
        self.assertFalse(Parenthesis("]").isValid())
        self.assertFalse(Parenthesis("[}]").isValid())
        self.assertFalse(Parenthesis("{()}]").isValid())


if __name__ == "__main__":
    unittest.main()
