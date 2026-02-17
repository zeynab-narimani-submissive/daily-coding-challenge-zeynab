from operator import truediv


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

print(is_palindrome("level"))
print(is_palindrome("low"))
