# example 1
def get_sum(numbers):
    sum_of_num = 0
    for i in numbers:
        num = int(i)
        sum_of_num += num
    return sum_of_num

numbers = [2,1,5,6]

sum_of_numbers = get_sum(numbers)
print(sum_of_numbers)
# example 2 
def get_reversed_string(string):
    output = string[::-1]
    return output
string = input()
resultant_string = get_reversed_string(string)
print(resultant_string)
# example 3 
def calculate_power(x, y):
    if y ==1:
        return x 
    else:
        y -= 1 
        return x * calculate_power(x,y)
a = int(input())
b = int(input())
result = calculate_power(a,b)
print(result)