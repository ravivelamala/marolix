# write a python program to find the sum of list elements.
list_a = input().split(" ")
sum = 0 
for i in list_a:
    i = int(i)
    sum += i
    
print(sum)