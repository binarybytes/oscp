


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











