#Exercise 19: Functions and Variables
#From Learn Python the Hard Way
#By Jessica Ice
#Created on May 15, 2016
#Last Edited on May 15, 2016

#This creates a function that tells me about a number of cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" %boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
#This runs the function with just number I input
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#This runs the function with variables I define
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#This runs the function with some math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#This runs the function with a combination of variables and math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#This is my Beyonce inspired function. 
def lemonade(x, y, z):
	print "Oh man Jay Z screwed up this time!"
	print "Why do you think that is?"
	thought = raw_input()
	print "Oh really %r? I thought it was because %s" %(thought, x)
	print "How old do you think Beyonce is?"
	b_age_guess = input()
	print "Actually she is %r years old. You are off by %r years." %(y, b_age_guess - y)
	print "You must be really embarrassed by your terrible guess."
	print "I will try to guess how old you are.. I bet I will be better."
	print "First you have to write how old you are here.. I'm not looking. I promise."
	your_age = input()
	print "Okay, I guess you are %r years old." % z
	print "Opps.. I am %r years off..." % (z - your_age)
	print "I guess I am not so smart after all."

lemonade("he tapped Becky with da good hair", 34, 26)

lemonade("he couldn't handle all that jelly", 30+4, 50)

lemonade("he is a little bitch", 34, 43)
