# check given string is palindrome or not 
# example 1 
sentence = input()
lower = sentence.lower()
sentence_2 = sentence[::-1]
if sentence == sentence_2:
    print("given sentence is palindrome")
else:
    print("given sentence is not palindrome")

