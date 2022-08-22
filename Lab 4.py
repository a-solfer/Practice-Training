# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:23:52 2021

@author: -
"""

#1 Q1. Print all positive numbers from the list
#[3, -5, 2, -1, 0, 7]

L=[3, -5, 2, -1, 0, 7]

#OPTION 1- not really
print(L[0],L[2],L[4],L[5])
print(L[0],L[2],L[4:])

#OPTION 2
for num in L:
    if num >=0: print(num)

#OPTION 3
    
def positiveonly(list):
    for num in list:
        if num>=0 :
            print(num)
positiveonly([3, -5, 2, -1, 0, 7])

#OPTION 4

List=[3, -5, 2, -1, 0, 7]
for num in List:
    while num >=0:
        print(num)
        break

print(" ")
print(" ")

#Q2. Create a text file with the following sentence:
#The fox jumped over the fence
#Read the text file and print each individual word.
#HINT: use for loop and the split function

file = open ("foxy.txt", 'w')
file.write('The fox jumped over the fence')
file.close()
#Read the text file
file = open("foxy.txt","r") 
for word in file:

    print (str.split(word))
    
    
    #ANOTHER WAY TO READ THE FILE
file = open("foxy.txt", "r") 
info = file.read()

for word in info.split():

    print (word)


print(" ")
print(" ")


#Q3. What will the following print?

for x in [1, 2, 3]:
    print(x)

print(" ")
print(" ")


#Q4. Write the python code to count how many
# es are there in the string Beetlejuice.

BJ="Beetlejuice"
print(word.count('e'))


print(" ")
print(" ")


#Q5. What will the output for the following be?

# hastags have been added to the example below
# because if run,
# there is no way to break the loop.

# print("Please give me a number: ")
# number=input()
# plusTen=number+10
# print("if we add 10 to your number, we get " + plusTen)

#The output gives a TypeError

#OPTION 1 using str when print
print("Please give me a number: ")
response=input()
number=int(response)
plusTen=number+10
print("if we add 10 to your number, we get " + str(plusTen))


#OPTION 2 using a , instead of str when print
print("Please give me a number: ")
response=input()
number=int(response)
plusTen=number+10
print("if we add 10 to your number, we get " ,plusTen)



print(" ")
print(" ")


#Q6. The if/elif/else structure is a ____________ structure.

print("multiple-selection")
print(" ")
print(" ")


# multiple selection
#Q7. The ________ module introduces the element of chance into Python programs.

print("Random")
print(" ")
print(" ")

##Q8. What will the ouput for the following?
import random

def generateNumber():
    return random.randrange( 0, 10 )
def generateQuestion( a, b ):
    return "How much is " + str( a ) + " times " \
+ str( b ) + "?"
wrong = 0 
while 1:
    if not wrong:

        number1 = generateNumber()
        number2 = generateNumber()
        answer = number1 * number2
        question = generateQuestion( number1, number2 )
        wrong = 0 
    print(question)
    response = input( "= " )
    if response == "q":
        break
    if int( response ) == answer:
        wrong = 0
        print ("Very good!")
    else:
        wrong = 1
        print ("No. Please try again.")
        
#ANSWER
#How much is 0 times 8 (#The numbers generated are random between 0 and 10)
# = (#wait for the users input ... lets say the user puts in  0)
# =0 (#the answer is correct)
# Very good! (#will Print as the ans is correct)

#OR

#How much is 0 times 8 (#The numbers generated are random between 0 and 10)
# = (#wait for the users input ... lets say the user puts in  8)
# =8 (#the answer is incorrect)
# No. Please try again. (#will Print as the ans is incorrect)
# = (#wait for the users input...)

#OR

#How much is 0 times 8 (#The numbers generated are random between 0 and 10)
# = (#wait for the users input ... lets say the user puts in  q)
# =q (#it will break the loop and the ques will not display again)

print(" ")
print(" ")

#Q9. Break the string into a list

string='The rain in Spain falls mainly in the plain'

#ANSWER1:
string='The rain in Spain falls mainly in the plain'
l=string.split(' ')

print(l)

#ANSWER2:

string='The rain in Spain falls mainly in the plain'
s = str.split(string)
print(s)


print(" ")
print(" ")


#Q10. Write a function that returns the maximum 
#of two numbers.

#ANSWER1:
def max(num1, num2):      
    if num1 >= num2:	
        return num1
    else:
        return num2
print(max(10, 5))


#ANSWER2:
def maximum(num1, num2):
	if num1>=num2:
		return num1
	if num2>num1:
		return num2
print(maximum(3,5))


answer = input("Enter string: ")
chars = list(answer)
numbers = list()
letters = list()

for x in chars:
   if (x.isdigit()):
       numbers.append(x)
   elif (x.isalpha()):
       letters.append(x)
 
print('Letters: ', len(letters))      
print('Digits: ', len(numbers))

difference = len(letters) - len(numbers)
print('Difference: ', len(letters), '-', len(numbers), '=', difference)