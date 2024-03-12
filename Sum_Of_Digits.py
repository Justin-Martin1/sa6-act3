sum_of_digits = lambda n: sum(int(digit) for digit in str(n))

number = 12345
print(f"Sum of digits of", number, ":", sum_of_digits(number))