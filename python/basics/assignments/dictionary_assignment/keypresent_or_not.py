# 2.Write a Python script to check whether a given key already exists in a dictionary.
students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}
key = input()
if key in students_dict:
    print("key present")
else:
    print("key not present")
