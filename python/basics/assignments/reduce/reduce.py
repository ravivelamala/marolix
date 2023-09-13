from functools import*
# sum of numbers
n = eval(input("enter a number: "))
event = reduce(lambda n,m:n+m,n)
print(event)
# multiply two numbers
n= eval(input("enter a number: "))
event = reduce(lambda n,m:n*m,n)
print(event)
# exponent and powers
num = eval(input("enter a number: "))
event = reduce(lambda m,n:m**n,num)
print(event)