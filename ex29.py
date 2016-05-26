#Exercise 29: What if 
#From Learn Python the Hard Way
#Created by Jessica Ice
#Created on May 25, 2016

#Creating some variables for the if statements
people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats: 
	print "Not many cats! The word is saved!"
	
if people < dogs:
	print "The word is drooled on!"
	
if people > dogs:
	print "The world is dry!"

#This is so that you will have equal number of dogs and humans	
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."
	
if people == dogs:
	print "People are dogs."
	
	
#This is a new game for me to write

print "What is your name?"
name = raw_input()

if name == "Jessica":
	print "Well don't you have the nicest name in the world!"
	print "How many pets do you have?"
	
if name != "Jessica":
	print "Okay how many pets do you have?"
	
pets = raw_input()

if pets == 0 and name != "Jessica":
	print "Wow, I feel so sorry for you. You have a sad life."
	
if pets == 0 and name == "Jessica":
	print "That's too bad, but at least you still have a cool name."
	
if pets > 0 and name != "Jessica":
	print "Ohhh.. how fun! Lucky you!"
	
if pets > 0 and name == "Jessica":
	print "I have to stop talking to you because I am too jealous of your life."