#!/bin/python3


#print string


print ("strings and things")
print ('hello0o0o')
print (''' hello
this is a multi line string''')
print ("this is "+" a string")



print ('\n') # new line


#math


print ("math time")
print (5+5) #add
print (5-5) #subtract
print (5*5) #multiply
print (5/5) #division

print (5+5-5*5/5) 
print (5 ** 2) # exponents
print (5 % 2) #modulo 
print (5 // 3) #number without leftover


print ("fun with titles and vars")

#variables

quote = "live laugh love"
print(len(quote)) #length
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title

 


name = "browski"
age = 32 #int
gpa = 3.5 #float



print (int(age))
print (int(29.9)) #does not round

#concatenations + types

print ("my name is " + str(name) + " and i am " + str(age) + " years old ")


print ('\n') #new line



age += 1
print (age)


birthday = 1
age += birthday
print (age)


#functions
print ("now , some functions ")
def who_am_i():
	name = "browski"
	age = 32
	print ("my name is " + str(name) + " and i am " + str(age) + " years old ")

who_am_i()


#adding in parameters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)


#add in multiple parameteres
def add(x,y):
	print(x + y)

add(7,7)
add(100,20)


#using return
def multiply(x,y):
	return x * y

print(multiply(7,7))

def square_root(x):
	return x ** .5

print(square_root(64))


print ('\n') #new line

#function for new line lulz
def nl():
	print ('\n')

nl

#boolean expressions (true or false)

#boolean expressions (true or false)


print("boolean expressions")

bool1 = True
bool2 = 3*3 == 9

bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)

print(type(bool1))


bool5 = "True"

print(type(bool5))

#relation + Bool operators

nl

greater_than = 7 > 5

less_than = 5 < 7

greater_than_equal_to = 7 >= 7

less_than_equal_to = 7 <= 7 

print(greater_than, less_than,greater_than_equal_to, less_than_equal_to)


test_and = (7 > 5) and (5 < 7) # one false makes it all false
test_or = (7 > 5) or (5 < 7) #only both false makes it false
test_not = not True # will be false 


print(test_and)


nl


#conditional statements



print("conditionals statements")


def soda(money):
	if money >= 2:
		return "You've got yo self a soda bruh!!!"
	else:
		return "no diabetes bruh!!"

print(soda(3))
print(soda(1))

nl

def alcohol(age,money):
	if (age >= 18) and (money >= 5):
		return "we gettin litttt!"
	elif (age >=18) and (money < 5):
		return "come back wit doh"
	elif (age < 18) and (money >= 5):
		return "nice try kiddo"
	else:
		return "u broke kiddie"

print(alcohol(18,5))
print(alcohol(18,4))
print(alcohol(17,4))


print(nl)

#lists (has brackets not parentheses)

print("lists have brackets")

movies = ["where harry met sally", "the hanvover", "flowers", "titanic"]

print(movies[0])

# numbering starts at 0, not 1

print(movies[0:2])
#you have to call the next number if you want the exact number

#slicing (up to but not including)

print(movies[1:]) #pulls starting from 1 till the end
print(movies[:1]) #pulls first item?
print(movies[-1])#pulls last item
print(len(movies))

movies.append("jaws")
print(movies)

movies.pop() #no number means rm last items
print(movies)


movies.pop(1)
print(movies)


movies = ["where harry met sally", "the hanvover", "flowers", "titanic"]

person = ["heath", "jake", "leah", "jef"]


combined = zip(movies, person)
print(list(combined))
#the above does a list in a list -- list inception, 



#tuples (has parentheses and are immutable - cant change)

print("tuples have parentheses and canNOT change!")

grades = ("A", "B", "C", "D", "F")
print(grades[1]) #will print B

#looping 

print("for loops - start to finish of iterate:")


vegetables = ["cucumber", "spinach", "carrot"]
for x in vegetables:
	print(x)


print("while loops - exe as long as True:")

i = 1
while i < 10: #while true, do smthing 
	print(i)
	i += 1

	









