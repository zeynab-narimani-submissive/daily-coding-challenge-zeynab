from operator import truediv
import unittest

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    reversed = ""
    neg = int("-" + str(len(cleaned)))
    i = -1
    while i >= neg:
        reversed += cleaned[i]
        i -= 1
    if s == reversed:
        return True
    else:
        return False

class TestPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("radar"))       # باید True باشه
        self.assertTrue(is_palindrome("level"))       # True

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))      # False
        self.assertFalse(is_palindrome("python"))     # False

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))            # رشته خالی پالیندرومه

    def test_with_spaces_and_case(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))  # True بعد از پاک کردن فاصله و بزرگ/کوچک

    def test_numbers(self):
        self.assertTrue(is_palindrome("121"))         # True
        self.assertFalse(is_palindrome("123"))        # False

if __name__ == '__main__':
    unittest.main()
