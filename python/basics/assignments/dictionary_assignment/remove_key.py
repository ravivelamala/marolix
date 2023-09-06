# Write a Python program to remove a key from a dictionary.
dict = {
    "physics" : 90,
    "math" : 95,
    "chemistry" : 100
}
remove_key = input()
if remove_key in dict:
    del dict[remove_key]
    print("key has been removed from dict")
else:
    print("given input not in dict list of items")
