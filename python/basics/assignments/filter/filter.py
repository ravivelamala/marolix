# even or odd 
event=eval(input('enter a numbers: '))
f=filter(lambda n : True if n%2==0 else False,event)
print(list(f))

print()
print()

# filter number is in between 1 to 100 or not
num=eval(input('enter a number: '))
f=filter(lambda n : True if 1<=n<=100 else False,num)
print(list(f))

print()
print()

# divisible by 3 and 5.
num=eval(input('enter a number: '))
f=filter(lambda n : True if n%3==0 and n%5==0 else False,num)
print(list(f))