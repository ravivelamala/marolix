# Write a Python program to convert a list of multiple integers into a single integer.
list_a = input("enter input: ").split(" ")
output = ""
for i in list_a:
    output += str(i)
print(output)