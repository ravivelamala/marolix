# List Methods: 1) append() 2) extend() 3) insert() 4) pop() 5) clear() 6) remove() 7) sort() 8) index()
# 1) Append() : Adds an element to the end of of the list.
# list.append(value)
list_a = []
for x in range(1,4):
    list_a.append(x)
print(list_a)
# Extend(): Adds all the elements of a sequence to the end of the list.
# list_a.extend(list_b)
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b)
print(list_a)
# insert(): Element is inserted to the list at specified index.
# list.insert(index,value)
list_a = [1, 2, 3]
list_a.insert(1,4)
print(list_a)
# pop(): Removes last element.
# list.pop()
list_a = [1, 2, 3]
list_a.pop()
print(list_a)
# Remove():  Removes the first matching element from the list.
# list.remove(value)
list_a = [1, 3, 2, 3]
list_a.remove(3)
print(list_a)
# clear(): Removes all the items from the list.
# list.clear()
list_a = [1, 2, 3]
list_a.clear()
print(list_a)
# index(): Returns the index at the first occurrence of the specified value.
# list.index(value)
list_a = [1, 3, 2, 3]
index =list_a.index(3)
print(index)
# count(): Returns the number of elements with the specified value.
# list.count(value)
list_a = [1, 2, 3]
count = list_a.count(2)
print(count)
# sort(): Sorts the list.
# list.sort()
list_a = [1, 3, 2]
list_a.sort()
print(list_a)