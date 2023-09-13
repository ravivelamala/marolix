# multiply numbers
num = eval(input("enter a number: "))
list_1 = list(map(lambda x:x*x,num))
print(list_1)
# multiply with a numbers
num = eval(input("enter a number: "))
list_2 = list(map(lambda x:x*5,num))
print(list_2)
# add a number
num = eval(input("enter a list of numbers: "))
add = list(map(lambda num:num+2,num))
print(add)