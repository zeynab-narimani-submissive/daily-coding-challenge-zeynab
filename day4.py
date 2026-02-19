def reverse_string(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)


# تست‌های ساده داخل فایل
if __name__ == "__main__":
    print(reverse_string("hello"))      # "olleh"
    print(reverse_string("زینب"))        # "بنیز"
    print(reverse_string(""))           # ""
    print(reverse_string("radar"))      # "radar"