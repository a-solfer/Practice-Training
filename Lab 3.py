# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 21:58:31 2021

@author: Admin
"""
# print(" ") will be used to seperate output tasks when needed.
#Task1- Print Hello Pything World
#because I am printing a constant I use double quotations
print("Hello Python World")
print(" ")

#Task2- Assign Hello Pything World to an identifier
#or variable called message and then print message
message= " Hello Python World"
#Now, to print it, I dont enclose message in quotations
#because message is a variable, If I were to enclose it
#then it would actually print the word message instead of 
#the value given to it which is "Hello Python World"
print(message)
print(" ")

#Task3- Assign Pything is my favorite language to a
# identifier or variable called message
# and then print message
# we are using the same identifier as the privous task
#this is not a problem as they can hold different values
#trouhout the program
message= "Python is my favorite language"
print(message)
print(" ")

#Task4- Assign message toa variable called word
#then print word
# it print Pythong is my favorite language because
#that was the last value it had
word=message
print(word)
print(" ")

#task5- Print Hello World on line 1 and 
# Hello World again! on line 2
#hint: \n

#ANS1
print("Hello World")
print("\nHello world again!")
print(" ")

#ANS2
print("Hello World \nHello world again!")
print(" ")

#ANS3
print ("Hello World")
print("Hello world again!")
print(" ")

#Ans4
#we use 3 quotations
print("""Hello World
      Hello world again!""")
print(" ")
      
      #if you do not want the indent, 
      #then just delete that space
      
print("""Hello World
Hello World again!""")
print(" ")
print(" ")
print(" ")

# PART 2 STRING MANIPULATION

#anything enclosed in your quotations are strings
#we can manipulate them

#string manipulation embarks
#Creation, Accessing, Lenght, Finding, Count, Slicing
#Split strings, Star swith/Endswith, Repeat strings, 
#Replacing, Changing upper and lower case strings,
#Concatenation, Join, Testing

#1-Accessing
#If I want to pick up specific characters from my strin
#we use the braquets [ ],with the  index value that you want. Index values
#the index value start at zero.
# A space is also a character

word= "Bonjour tout le Monde"
print(word)

letter=word[0] 
print(letter)
print(" ")

#2- Lenght
#it will count how many characters 
#you have in your string

example="two words"

len(example)
print(" ")

#3-Finding
#I can look up how many times a character appears
#in my string

Hello="Bonjour"
print(Hello)

print(Hello.count("o"))
print(" ")

word= "Bonjour tout le Monde"
print(word)

print(word.count("n"))
print(" ")

#if you use the option "find" instead of "count"
#then the result will give you the POSITION of 
#that character

print(word.find("B"))
print(" ")

#the result is 0 because B is the first letter 
#in position 0

#On the other heand, If you use "index" it will give
#the position of the first instance it came in
#contact with what you are looking for

#example

fruit="I like Grapefruit"
print(fruit)
print(fruit.index("Grapefruit"))
print(fruit.index("pefruit"))
print(fruit.index("like"))

#the result is seven because the G isthe 7th character
#including spaces.( remember, we start form 0)

print(" ")
print(" ")

#4-COUNT

#it will count the number of spaces in a string

favorite="color is green"
print(favorite.count(" "))

three="three spaces this time"
print(three.count(" "))

four="    "
print(four.count(" "))

print(" ")
print(" ")

#5-SLICING

#It is to get specific characters from your string
#that will give you a set of letter 

word="Hello World"

print(word[0])
print( word[0:1]) #this one and the one above are the same
print(word[0:4])
print(word[:4]) #this one is the same as #3
print(word[-3:]) #it will start counting from the end

#if you do [3:] that means, ignore the 
#first 3 characters and get everything after

print(word[3:])

#the one below is, get me all the characters
#except the last three

print(word[:-3])

movie="Star Wars"
movie[:] #if left blank, it copies everything


print(" ")
print(" ")
#6-SPLIT STRING:
#i can split it in multiple columns
    
#2021-02-01 17:36"15 ABCDEFG
#1. Assign the above to a variable called str
#2. The output should print 02012021

str='2021-02-01 17:36"15 ABCDEFG'

#time on video: 1:12:03 for the exercise above



#STRINGS

print(" ")
print(" ")

#String Manipulation
#creation

#Task5-  Print Hello world on line 1 
#and Hello world again on line 2

#ANS1

print("Hello world")
print("\nHello World again")
print(" ")

#ANS2
print(" Hello world \nHello world again")
print(" ")

#ANS3

print("Hello world")
print("Hello world again")
print(" ")

#ANS4

print(''' Hello World
          Hello World again!''')
print(" ")         
print(" ")

#TASK8 - Change Cases
#1. Assign eric to variable called fist_name & print it
#2. Change the case to UPPER case and print it

#ANS1 - Printed in Upper case
first_name="eric"
print(first_name)
print(" ")

print(first_name.upper())
print(" ")

#ANS2 - Printed in title case

print(first_name.title())
print(" ")

#ANS3 - Printed in upper case

print(first_name), print(first_name.upper())
print(" ")

#TASK9 - Concatination
#1. Assign ada to fist_name
#2. Assign lovelace to last_name
#3. Concatinate first_name and last_name in a
#variable called full_name
#4. print full_name in title case

first_name="ada"
last_name="lovelace"
full_name= first_name + last_name
print(full_name.title())
print(" ")
#Ans2

first_name="ada"
last_name="lovelace"
full_name= first_name + " "+ last_name
print(full_name.title())
print(" ")


#SLICING:

word="Bonjour mes amis"
print(len(word))
len(word)
print(word[1] +  word[5] +word[6] + word[15])
print(" ")  

#LISTS

royals=['Francesca','Rachel','Andrew','Anthony']
print(royals)
print(royals[2])
print(" ")

#SLICING:
print(royals[:2])

len(royals)
royals.append('Jen')
print(royals)

royals.insert(3,'Dave')
print(royals)

honorary=['Mimi','Lucille','Jolie','Barney']
royals.extend(honorary)
print(royals)

print(royals)
royals.remove('Barney')
print(royals)




