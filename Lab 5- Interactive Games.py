# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:22:32 2021

@author: sheemam
"""

#TASK1 - MODULES
#1. Ask the user to input a number
#2. If the number is met print Correct in ___ tries
#3. if its not met print Higher or Lower
#4. For the number import the following modules/libraries
#   random and math
#   use the random function to get a random number 
#   multiply the number by 100 and add 1 to it

### WHAT WE HAD DONE ###
number=45
count=0
while True:
    count +=1
    guess=int(input("Guess the secret number: "))
    if number > guess:
        print("Higher")
    elif number < guess:
        print("Lower")
    else:
        print("Correct! in", count, "tries.")
        break

### END WHAT WE HAD DONE ###

#ANSWER1
import random, math
random.seed()
x=math.floor(random.random()*100)+1
z=0
b=0
while x!=z:
    b=b+1
    z=float(input("Guess the secret number: "))
    if z < x: print("Higher!")
    if z > x: print("Lower!")
print("Correct! in", b, "tries.")

### to check what is in the Math Module/Package
import math
content =dir(math)
print(content)

import random
content =dir(random)
print(content)


#TASK2 - Create a 8Ball program
#1. Create a file called 8ball.config. Enter some options
#2. Write the 8Ball python code to read the options and randomly 
#   display an option from the 8ball.config file in answer to the 
#   users question
#HINT: file object, random, dict, for, input

import random
magicball={}
counter=0
#Import and Read the 8ball.cofig file
#Build the dict containing all the possible answers
file=open("8ball.config")
for line in file:
    magicball.update({counter:line.split("\n")[0]})
    counter +=1
print("Seeing into", counter, "possible futures.")
input("Ask the Magic 8 Ball a question: ")
answerkey=random.randrange(counter)
print("")
print("")
print(magicball[answerkey])

#FILE 2 *******  MODULES AND IO  ************************

#TASK1 - Read and Write to a CSV file
#HINT: import the csv module, for, with, lists, 
#       various file methods

import csv 
fields=['Name', 'Branch', 'Year', 'GPA']
rows=[['Larry', 'Engg', '2', '3.1'],
      ['Curley', 'IT', '1', '3.5'],
      ['Moe', 'Math', '2', '3.1'],
      ['Kelly', 'MIS', '1', '3.3'],
      ['Jill', 'Mgmt', '3', '2.8'],
      ['Sabrina', 'CS', '2', '3.1']]
filename="university_records.csv"
with open(filename, 'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

#Read the csv file
with open("university_records.csv", newline='') as f:
    reader=csv.reader(f)
    for line in reader:
        print(line)

# Remove the Extra Blank rows/lines of data
with open("university_records.csv") as input, open("university_records1.csv", "w") as output:
    no_blank=(line for line in input if line.strip())
    output.writelines(no_blank)
 
#Read the New csv file        
with open("university_records1.csv", newline='') as f:
    reader=csv.reader(f)
    for line in reader:
        print(line)
        

#TASK2 - Download Data from the web
#1. import urllib
#2. Write the main function
#3. declare a variable called webURL
#4. Call the urlopen function from the urllib module
#5. Open a site (http://www.cnn.com)
#6. Read the data and print it
        
import urllib
#open the connection
webURL=urllib.request.urlopen("http://www.cnn.com")
#Test the connection - Result code should be 200
print("result code: "+ str(webURL.getcode()))
data=webURL.read()
print(data)

##Open a secure site (https)
import urllib
#open the connection
webURL=urllib.request.urlopen("https://finance.yahoo.com")
#Test the connection - Result code should be 200
print("result code: "+ str(webURL.getcode()))
data=webURL.read()
print(data)


#FILE 3 ***** MODULES  FUNCTIONS  IFS  COLORGAME  **********

#TASK1 - Working with Modules, Functions, Loops, IFs, 

#import the Modules
import tkinter, random
#Create a list of the possible colors
colours=['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White','Purple', 'Brown']
score=0
#the game time feft, initially 30 seconds
timeleft = 30
#function that will start the game
def startGame(event):
    if timeleft ==30:
        #start the countdown times
        countdown()
    #run the function to choose the next color
    nextColour()
#Function to choose and display the next Color
def nextColour():
    #use the globally declared variables 'score' and 'timeleft'
    global score
    global timeleft
    #if the game is currently in play
    if timeleft >0:
        #make the test entry box active
        e.focus_set()
        #if the color typed is equal to the color of the text increase the score
        if e.get().lower()==colours[1].lower():
            score+=1
        #Clear the entry box 
        e.delete(0, tkinter.END)
        #Change the color to type, by changing the text and 
        #the color to a random color value
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        #Display the score
        scoreLabel.config(text="Score: "+ str(score))
#Countdown timer function
def countdown():
    global timeleft
    #if the game is currently in play
    if timeleft >0:
        #decrement the timer
        timeleft -=1
        #update the timeleft label
        timeLabel.config(text="Time Left: "+ str(timeleft))
        #run the function again after 1 second
        timeLabel.after(1000, countdown)
#Driver Code
#Create the GUI (window)    
root = tkinter.Tk()
#set the title for the GUI
root.title("COLORGAME")
#set the size
root.geometry("375x200")
#add the instructions label
instructions=tkinter.Label(root, text="Type in the color of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()
#add the score label
scoreLabel=tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()
#add the time left label
timeLabel=tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()
#add the label for displaying the colors
label=tkinter.Label(root,  font=('Helvetica', 60))
label.pack()
#add a text entry box to type the colors
e=tkinter.Entry(root)
#Run the startGame function when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()
#set the focus on the entry box
e.focus_set()
#start the GUI
root.mainloop()


#FILE4********** MODULES  READING  CVS  WINEQUALITY ********************

#TASK1 - 
#1. import the csv library/module
#2. open winequality-red.csv
#3. Create the csv reader object
#4. pass the delimeter ; to the argument so it allows you to read
#   and split the data from the csv file
#5. Call the list type to get all the rows from the csv file
#6. Assign the values to a variable called wines
#7. Print out the first 3 rows

#ANSWER1
import csv 
with open("winequality-red.csv", newline='') as f:
    reader=csv.reader(f)
    x=0
    varible=[]
    for line in reader:
        x+=1
        varible.append(line)
        if x==3:
            break
    print(varible)
    
#ANSWER2
import csv
with open("winequality-red.csv", 'r') as f:
    wines=list(csv.reader(f, delimiter=";"))
print(wines[:3])


#TASK2
#1. Extract the last element from each row after the header row
#2. Convert each extracted element to float
#3. Assign all the extracted elements to a list called qualities
#4. Divide the sum of all the elements in the qualities by
#   the total number of elements in quality to get the mean
#5. Print the mean

#ANSWER1
import csv 
with open("winequality-red.csv", 'r') as f:  
    x=0
    counter=0
    wines=list(csv.reader(f,delimiter=';'))
    for i in wines[1:]:
        for y in i[-1]:
            y=float(y)
            x+=y
            counter+=1
    average= x/counter
    print(average)


#ANSWER2
import csv
with open("winequality-red.csv", 'r') as f:
    wines=list(csv.reader(f,delimiter=';'))
qualities=[float(item[-1]) for item in wines[1:]]
a=sum(qualities)/len(qualities)
print(a)




#TASK3 - Create a numpy array using the numpy.array function
#Pass it in a list of lists so it will automatically create a 
#numpy array with the same number of rows and cols
#we want all the elemts in the array to be a float for
#easy computation, leave off the header row

#ANSWER1
import numpy as np
wines=np.array(wines[1:], dtype=np.float)
print(wines)

#TASK4 - Retrieve the value from the 4th col and 3rd row
print(wines[2,3])

print(wines[2],[3])



















