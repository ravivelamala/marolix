# write a program to create a calculator using functions
def add(x,y):
    return x + y 
def subtract(x,y):
    return x - y  
def multiply(x,y):
    return x * y  
def divide(x,y):
    return x / y  

def calculator():
    print("options")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
option = input("enter a option: ")
num1 = float(input("enter a number1: "))
num2 = float(input("enter a number2: "))

if option == "1":
    print("result: ", add(num1,num2))
elif option == "2":
    print("result: ",subtract(num1,num2))
elif option == "3":
    print("result: ",multiply(num1,num2))
elif option == "4":
    print("result: ",divide(num1,num2))
else:
    print("invalid input")


