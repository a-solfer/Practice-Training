# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 23:02:03 2021

@author: Owner
"""

#TASK1
print("\nWelcome to the fitness center. What would you like to do?")

#Set an initial value for the choice

choice =''
confirm=''

#Start the loop that runs until q (while loop)

while choice !='q':

    print("\n[1] Enter 1 to take a bike ride.")

    print("[2] Enter 2 to go for a run.")


    print("[3] Enter 3 to climb a mountain.")

    print("[4] Enter 4 to go swimming.")

    print("[q] Enter q to Quit!.")

#Ask the user's choice (input)

    choice=input("\nWhat would you like to do? ")

#Respond to the users choice (IF and elif)

    if choice == '1':
        print("\n Here's your bike. Grab a helment from the rack. Have fun!\n")
    elif choice == '2':
        print("\n Here are some sneakers. Run fast!\n")
    elif choice == '3':
        print("\n Here's a map. Can you leave a trip plan for us?\n")
    elif choice == '4':
        print("\n Don't pee in the pool. Good Luck!\n")
    elif choice == 'q':
        confirm=input("\n Are you sure? Type y to quit and n to continue playing")
        if confirm =='y':
            print("\n Thanks for playing. See you later.\n")
            break
        if confirm =='n':
            print("Let's continue playing!")
            choice=''
    else:
        print("\n I don't understand that choice, please try again. \n")

#Print message that we are done!!

print("Thanks again, bye now.")


#TASK2

#Favorite Colors

#Write a function that takes two arguments, 
    #a person's name and their favorite color. 
    #The function should print out a statement 
    #such as "Hillary's favorite color is blue."

#Call your function three times, 
    #with a different person and color each time.

def name_color(color, name):
    """ Which color is their favorite?."""
    print("\nThe color " + color + " is " + name + "'s favorite")
    
name_color('orange', 'Emily')
name_color('brown', 'Dean')
name_color('lilac', 'Khoren')


#Task3

def phone_brand(phone, brand):
    """ What phone do you have?"""
    print("\nThe " + phone + " was made by " + brand)
    
phone_brand('Iphone xr', 'Apple')
phone_brand('Samsung Galaxy A42 5G', 'Samsung')
phone_brand('razr (2nd gen)', 'Motorola')


#TASK4

#Write a function that adds the given numbers 
    #together and prints the sum.

#Then add any other numbers that were sent to
#    the arbitrary number of arguments 
    #and print the results
 
#HINT: * is needed for arbitrary number of arguments

#Example: if your numbers are (1, 2, 3)
# the output should be: The sum of your numbers is 6


def numbers(num_1, num_2):

    sum = num_1 + num_2
    print("the sum total of the numbers is: %d " % sum)

numbers(3, 5)
numbers(4, 2)
numbers(1, 8)
    
























