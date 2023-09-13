# to add two numbers using lambda function
num1 = int(input("enter num: "))
num2 = int(input("enter num: "))
add = lambda num1,num2 : (num1+num2)
print(add(num1,num2))
# check even or odd
num1=int(input("enter a number1: "))
num2=int(input("enter a number2: "))
event=lambda num1,num2 : 'even' if (num1+num2)%2==0 else 'odd'
print(event(num1,num2))
# product of two numbers
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
product = lambda num1,num2: num1 * num2
print(product(num1,num2))
