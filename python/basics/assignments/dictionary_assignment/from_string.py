# Write a Python program to create a dictionary from a string.
sample_string = "marolix technology"
count_numbers = {}
for char in sample_string:
    if char.isalpha():
        char = char.lower()

        if char in count_numbers:
            count_numbers[char] += 1
        else:
            count_numbers[char] = 1 
print(count_numbers)