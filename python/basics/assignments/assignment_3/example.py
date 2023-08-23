# comparing the strings
# example 1
sentence_1 = "python is easy to understand"
sentence_2 = "day by day python demand increases"
length_1 = len(sentence_1)
length_2 = len(sentence_2)
if length_1 > length_2 :
    print("sentence_1 is bigger")
else:
    print("sentence_2 is bigger")
# example 2 

sentence_1 = "python is easy to understand"
sentence_2 = "day by day python demand increases"
length_1 = len(sentence_1)
length_2 = len(sentence_2)
if length_1 ==  length_2 :
    print("given sentence are equal")
else:
    print("given sentence are not equal")

# example 3 
 
sentence_1 = "python is easy to understand"
sentence_2 = "day by day python demand increases"
id_1 = id(sentence_1)
id_2 = id(sentence_2)
if id_1 != id_2 :
    print("True")
else:
    print("False")