strings = ["banana", "apple", "grape", "kiwi", "orange", "pear"]

sorted_strings = sorted(strings, key=lambda x: (len(x), x))

print("Sorted strings:", sorted_strings)