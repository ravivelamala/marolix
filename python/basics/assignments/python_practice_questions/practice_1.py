# 1.Write a program to reverse an integer in Python. 
number = int(input("Enter an integer: "))

is_negative = False
if number < 0:
    is_negative = True
    number = -number


reversed_number = int(str(number)[::-1]) * (1 if not is_negative else -1)

print(f"Original Number: {number}")
print(f"Reversed Number: {reversed_number}")

# 2.Write a program in Python to check whether an integer is Armstrong number or not. 
num = int(input("Enter an integer: "))

num_str = str(num)
num_digits = len(num_str)

sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)


if sum_of_digits == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# 3. Write a program in Python to check given number is prime or not. 

num = int(input("Enter an integer: "))

if num < 2:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

   
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

# 4. Write a program in Python to print the Fibonacci series using iterative method. 

num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

first_term = 0
second_term = 1

# 5. Print the Fibonacci series using an iterative method
print("Fibonacci Series:")
for _ in range(num_terms):
    print(first_term, end=" ")
    next_term = first_term + second_term
    first_term, second_term = second_term, next_term

# 6. Write a program in Python to print the Fibonacci series using recursive method. 

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


num_terms = int(input("Enter the number of terms in the Fibonacci series: "))


print("Fibonacci Series:")
for i in range(num_terms):
    print(fibonacci_recursive(i), end=" ")

# 7. Write a program in Python to check whether a number is palindrome or not using iterative method.

num = int(input("Enter an integer: "))


num_str = str(num)


start, end = 0, len(num_str) - 1


is_palindrome = True
while start < end:
    if num_str[start] != num_str[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1


if is_palindrome:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

# 8.Write a program in Python to check whether a number is palindrome or not using recursive method.

def is_palindrome_recursive(num_str, start, end):
    if start >= end:
        return True
    if num_str[start] != num_str[end]:
        return False
    return is_palindrome_recursive(num_str, start + 1, end - 1)

# Input integer
num = int(input("Enter an integer: "))

# Convert the number to a string for comparison
num_str = str(num)

if is_palindrome_recursive(num_str, 0, len(num_str) - 1):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

# 9. Write a program in Python to find greatest among three integers.

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))


greatest = max(num1, num2, num3)


print(f"The greatest among {num1}, {num2}, and {num3} is: {greatest}")

# 10. Write a program in Python to check if a number is binary? 

num = input("Enter a number: ")

is_binary = all(bit in '01' for bit in num)

if is_binary:
    print(f"{num} is a binary number.")
else:
    print(f"{num} is not a binary number.")

# 11. Write a program in Python to find sum of digits of a number using recursion? 

def sum_of_digits_recursive(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits_recursive(number // 10)

num = int(input("Enter a number: "))

sum_of_digits = sum_of_digits_recursive(num)

print(f"The sum of digits of {num} is: {sum_of_digits}")

# 12. Write a program in Python to swap two numbers without using third variable? 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After swapping, num1 is: {num1}")
print(f"After swapping, num2 is: {num2}")

# 12. Write a program in Python to swap two numbers using third variable? 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

temp = num1
num1 = num2
num2 = temp

print(f"After swapping, num1 is: {num1}")
print(f"After swapping, num2 is: {num2}")

# 13. Write a program in Python to find prime factors of a given integer.

num = int(input("Enter an integer: "))

factors = []
while num % 2 == 0:
    factors.append(2)
    num //= 2

for i in range(3, int(num**0.5) + 1, 2):
    while num % i == 0:
        factors.append(i)
        num //= i

if num > 2:
    factors.append(num)

print(f"Prime factors of {num}: {factors}")




