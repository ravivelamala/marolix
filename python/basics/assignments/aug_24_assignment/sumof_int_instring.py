# find sum of integers in the string 
word = input()
sum = 0

for i in word:
    if i.isdigit():
        sum += int(i)
       

print(sum)
