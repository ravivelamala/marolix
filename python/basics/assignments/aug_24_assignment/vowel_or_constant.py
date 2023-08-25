# given sentence is vowel or constant 
sentence = "aeiou"
word = input()
if word.isalpha() :
    if word in sentence:
        print("vowel")
    else:
        print("constant")
else:
    print("Invalid input")