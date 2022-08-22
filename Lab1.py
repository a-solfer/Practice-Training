# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:18:29 2021

@author: Admin
"""
#BEFORE starting, I will put a \n to seperate different tasks
#so when you print it, it looks more organized (it helps me too)
#Task1 Hello World-variable
variable="Hello World \n"
print(variable)

#Task2 One variable, 2 messages
message="Hope this works..."
print(message)

message="it worked!\n"
print(message)

#Task3- Someone said
quote="""Thoreau once said:
"I went to the woods because 
I wished to live deliberately,
to front only the essential facts of life.
And see if I could not learn what it had to teach,
and not, when I came to die,
discover that I had not lived."\n """
print(quote)

#Task4- First Name cases
#Lowercase
first_name="gimli"
#option1
print(first_name)
#or
print(first_name.lower())

#Title ase
print(first_name.title())

#Uppercase
print(first_name.upper())

#Task5 Full Name
first_name="sam"
last_name="gamgee"
full_name= first_name +" " + last_name
print(full_name.title())

#Task6 about this person
first_name="Oliver"
last_name="Sacks"
about_him= first_name+" "+ last_name + " was a renowned neurologist."
print(about_him)

#Task7 Name strip
name=' '"gandalf"' '
print(name)
print(" ".join(name))
#trip left side
print(name.lstrip())
#strip right side
print(name.rstrip())
#strip both sides
print( name.strip())

#option 2
name2= "  legolas  "
print(name2)
#trip left side
print(name2.lstrip())
#strip right side
print(name2.rstrip())
#strip both sides
print( name2.strip())

#option 3
name3="\n\tGollum\t\n"
print (name3)
#trip left side
print(name3.lstrip())
#strip right side
print(name3.rstrip())
#strip both sides
print( name3.strip())

#Task8 Arithmetic
#Write a program that prints out the results 
#of at least one calculation for each of the 
#basic operations: addition, subtraction, 
#multiplication, division, and exponents.

#addition
sum= 6+4
print(sum)

#subtraction 
sub= 6-4 
print(sub)
#multiplication
mult=6*4
print(mult)
#division
div= 6/4
print(div)
#exponents
expo=6**2
print(expo)

#Task9 Order of Operation

#Find a calculation whose result depends
#on the order of operations.

#Print the result of this calculation using
#the standard order of operations.

#Use parentheses to force a nonstandard order of operations.

#Print the result of this calculation

std_order= (7+3 * 2)
print(std_order)

my_order= ((7+3) * 2)
print(my_order)

#Task10 Long Decimals
#On paper, 0.1+0.2=0.3. But you have seen that in Python
#0.1+0.2=0.30000000000000004
#Find at least one other calculation 
#that results in a long decimal like this.

print(0.2*0.1)

#Task11 Neat Arithmetic

#Store the results of at least 5 different calculations
    #in separate variables.
#Make sure you use each operation at least once.
#Print a series of informative statements
#Such as "The result of the calculation 5+7 is 12."

calc1= 1+3
calc2= 2*4
calc3= 6-4
calc4= 4/2
calc5= 9**2
print("the sum of 1+3 is equal to:", calc1)
print("when we multiply 2x4 we get:", calc2)
print("when we substract 4 from 6 the result is:", calc3)
print("the division of 4 by 2 yields:", calc4)
print("the result of elevating 9 to the power of 2 is:", calc5)

#Task12
#Instead of just printing the results, print an
#informative summary of the results. 
#Show each calculation that is being done 
#and the result of that calculation. 
#Explain how you modified the result using parentheses.

#retrieved from task 9

std_order= (7+3 * 2)
print(std_order)

my_order= ((7+3) * 2)
print(my_order)

print(""" In the first calculation labeled std_order,
      the program assumes the basic rules of math
      which declare that multiplying has a higher
      hierarchy than sum or substraction.
      \nTherefore,the porgram will multiply 3 x 2 before adding seven
      to the result giving us:""",std_order,
      """Nonetheless, parenthesis have a higher hierarchy
      than multiplication and are calculated before anything
      else. Thus the reason why by enclosing 7+3 in them
      the program will calculate these first instead.
      Once the result is given, the program will multiply it by 2
      giving us as result:""", my_order)
      
#Task13 Long Decimal Pattern
var1=0.2+0.1
print(var1)

var1b=(0.2+0.3)
print(var1b)
      
var2=0.2*0.1
print(var2)

var3=0.2/0.1
print(var3)

#I am not sure how to find the pattern but I notice
#that as long as it is the number 0.1 and 0.2 it works (with sum and division)
#but not necessarily if the number increases such as 0.3