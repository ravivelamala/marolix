#  Write a Python program to sum all the items in a dictionary.
my_dict = {
    "a" : 10,
    "b" : 20,
    "c" : 30,
    "d" : 40
}
sum = 0 
for char in my_dict.values():
    sum += char 
print(sum)
