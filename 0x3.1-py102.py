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

letter = "a"
word = "Apple"
print(letter.lower() in word.lower()) #improved - case insensitive

word_two = "bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower())) #true and not false is True and True


too_much_space = "	hello	"
print(too_much_space.strip( )) #cuts out the space

full_name = "eo matrix"
print(full_name.replace("eo", "neo")) #replaces
print(full_name.find("matrix"))


#placeholders

movie = "the hangover"
print("my fav movie is {} " .format(movie))

def fav_book(title,author):
	fav = "my fav book is \"{}\", which is written by {}." .format(title,author)
	return fav


print(fav_book("great gatsby","f.scott fitzgerald"))


nl()


#dictionaries 
print("dictionaries are keys and values:")



#[] lists
#() tuples
#{} dictionaries


drinks = {"white russians": 7, "old fashion": 10, "lemon drop": 8, "butthead": 6} #drink is key, price is value
print(drinks)

nl()

employees = {"finance": ["bob", "linda", "tina"], "IT": ["gene", "louse", "teddy"], "HR": ["jimmy", "mort"]}
print(employees)

nl()

employees["Legal"] = ["mr.frond"] #add new key: value pair
print(employees)

nl()

employees.update({"sales" : ["andie", "ollie"]})
print(employees)

nl()

drinks["white russians"] = 8
print(drinks)


print(drinks.get("white russians"))


print(drinks.get("martini")) #get smt tht doesnt exist, returns None

print(drinks["white russians"])

#list and dictionaries 
movies = ["harry", "hangover", "flowers", "titanic"]
person = ["heath", "bob", "leah", "heff"]
combined = zip(movies, person)
movie_dictionary = {key: value for key, value in combined}


print(movie_dictionary)







