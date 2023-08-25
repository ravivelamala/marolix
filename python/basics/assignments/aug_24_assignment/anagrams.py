# to check string in anagrams or not 
sentence = input()
word = input()
count = 0
if len(word) == len(sentence):
    for char in sentence:
        if char in word:
            if sentence.count(char) == word.count(char):
                count += 1
    if count == len(sentence):
        print("given string is a anagram")
    else:
        print("given string is not anagrams")
else:
    print("invalid input")

