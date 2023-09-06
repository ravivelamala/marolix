# Write a Python program to iterate over dictionaries using for loops
students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}
for items in students_dict.items():
    print(items)
for key in students_dict.keys():
    print(key)
for value in students_dict.values():
    print(value)