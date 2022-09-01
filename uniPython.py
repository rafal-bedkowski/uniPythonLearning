# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:46:55 2022

@author: Rafał
"""
import math

#--------Variables----------#

#String 
# name = 'Al' v name= "Al"

#int
#age = 21 whole numbers

#float
#height = 250.5 whole with decimal points

#height = 250.1
#print(str(height)) we use casting float to string

#boolean
#true or false

#-----MULTIPLE ASSIGNMENT-----#
#multiple assignment --> allows us ti asign multiple variables at the same time in one line of code
#name, age, attractive = "Bro", 21, True

#Elen =30
#Al=30
#Bro = 30
#Adam = 30
#Elen=Al=Bro=Adam=30

#-----STRING METHODS----------#

name = "bro code"
name2 = 'BROCODE'

#len --> gives the length of a strng
print(len(name))

#find --> find the index where the searching letter is positioning
print(name.find("r"))

#capitalized --> make the first letter of a astring capitalize(bigger)
print(name.capitalize())

#upper --> make a whole string upper case
print(name.upper())

#lower --> make string lower case
print(name2.lower())

#isdigit --> show is our string is a digit, return true or false
print(name.isdigit())

#isalpha --> show is our string i alphabetical characters
#it will show error if there will be space bettwen word
print(name2.isalpha())

#count --> count the number of the character in a string
print(name.count('o'))

#replace --> we replace the character in the string
print(name.replace('o', 'a')) #first is old character second on what character we want to change

#multiple string --> not exactly a function but can multiple our string
print(name*3)

#---------TYPE CASTING--------#

#type casting --> convert the data type to another data type

x= 1
y= 2.0
z = '3'

print(str(x))
print(str(y))
print(int(z))

#--------INPUT USER-----------#

#allows user to input data into console

#name = input("Hello my man, please enter your name: ")
#age = int(input("How old are you?: "))

#age = age + 1
#print("hello " + name + " you are " + str(age) + " years old")

#--------MATH FUNCTION---------#  

pi = 3.14

#round -->round the number to the nearsest whole integer
print(round(pi))

#ceil --> math function that round number to up, whole integer
print(math.ceil(pi))

#abs --> absolute value, show how far the number is from zero
print(abs(pi))

#pow --> power the number to the power we declared
print(pow(pi, 2))

#sqrt --> in math module you can find it, count square root of a number
print(math.sqrt(pi))

#max --> will find the highest value from all the variables we put
x =12
y=17
z= 14

print(max(x, y, z))

#min --> will find the smallest number from variable we given
print(min(x, y, z))

#--------STRING SLICING--------#

#slicing create a substring by extracting elements from another string
# indexing[] or slice()--> slice is a method
#slicing usage [start:stop:step]

#first index is inclusive, the stop index is exclusive, so we always have to give one more, to include element we want to
name = 'Edgar Huffelpuff'
first_name = name[0:5]
last_name = name[6:16]
funky_name = name[0:16:2] #we count all second letter from the string and crate a new substring

reversed_name = name[::-1] #minus allows us to go backward, from the last letter of the string to the frist one

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)




