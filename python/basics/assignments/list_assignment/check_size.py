# write a python program to check the sizes of given two lists are same.
user_input1 = input("Enter the first list separated by commas: ")
user_input2 = input("Enter the second list separated by commas: ")

if len(user_input1) == len(user_input2):
    print("The sizes of the two lists are the same.")
else:
    print("The sizes of the two lists are different.")
