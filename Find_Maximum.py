def find_maximum(numbers, compare):
    max_number = numbers[0]
    for num in numbers:
        max_number = compare(max_number, num)
    return max_number

numbers = [3,7,2,9,5]
maximum = find_maximum(numbers, lambda x, y: x if x > y else y)
print("Maximum number:", maximum)