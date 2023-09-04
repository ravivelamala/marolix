# Write a Python function that takes two lists and returns True if they have at least one common member.

def list_check():
    list_a = input("enter list: ")
    list_b = input("enter list: ")
    for char in list_a:
        if char in list_b:
            return(True)
            break
        
    else:
        return(False)
print(list_check())

print()
print()

# Write a Python program to remove a specified column from a given nested list.
list_a=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
list_1=[]
for i in range(int(len(list_a))):
    element=list_a[i]
    element.pop(0)
    list_1.append(element)
print(f'new list after removing specified elements: {list_1}')

print()
print()
    
