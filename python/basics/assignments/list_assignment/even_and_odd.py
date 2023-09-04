# write a python program to print even and odd numbers seperatly in list.
list_a = input().split(" ")
even = []
odd = []
for i in list_a:
    i = int(i)
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)