import unicodedata

def reverse_string(s):
    # اول normalize به NFC تا ترکیب‌ها یکی بشن
    normalized = unicodedata.normalize('NFC', s)
    chars = list(normalized)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)

