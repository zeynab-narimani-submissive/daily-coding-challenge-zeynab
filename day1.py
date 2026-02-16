def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num
numbers = []
for i in range(10):
    numbers.append(int(input("input numbers")))
print(find_max([3,1,4,1,5,9,2,6]))
print(find_max(numbers))
