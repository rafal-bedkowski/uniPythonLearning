# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:46:55 2022

@author: Rafał
"""


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

input("Hello my man, please enter your name: ")