# count alphabets and digits and special characters in given string 
sentence = input()
alphabets = 0 
digits = 0 
special_char = 0 
for char in sentence:
    if char.isalpha():
        alphabets += 1 
    elif char.isdigit():
        digits += 1 
    else:
        special_char += 1 
print(alphabets)
print(digits)
print(special_char)


   