#!/bin/python3

#importing

print("importing is important!")


import sys #system functions and parameters
from datetime import datetime


print(datetime.now())


from datetime import datetime as dt #importing with alias

print(dt.now())

def nl():
	print ('\n')

nl()

#advanced strings

print("advanced strings")
my_name = "nick"
print(my_name[0]) #first initial
print(my_name[-1]) #last inital

sentence = "this is a sentence."

print(sentence[:4]) #captures this
print(sentence[-9:-1]) #can also go backwards
print(sentence[-0]) #just the first inital 


print(sentence.split()) #split by delimiter (space)

sentence_split = sentence.split()
sentence_join = " " .join(sentence_split)
print(sentence_join)
print ('\n'.join(sentence_split))


quoteception = "I said i wil give all the money"
print(quoteception)

quoteception = "i said, \"give me all the money\"" #char escape
print(quoteception)

print ("A" in "Apple") #boolean True

letter = "A"
word = "Apple"












