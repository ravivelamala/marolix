# remove repeated character from string 
sentence = input()
result = ""
repeat = set()
for char in sentence:
    if char not in repeat:
        result += char 
        repeat.add(char)
print(result)
