#Exercise 18: Names, Variables, Code, Functions
# From Learn Python the Hard Way
#Created by Jessica Ice
# Created on May 14, 2016
# Last edited on May 14, 2016

# We are learning about functions - they do three things:
# 1 - they name pieces of code the way variables name strings and numbers
# 2 - They take arguments the way your scripts take argv
# 3 - Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands"

# You use "def" to create functions in python

#this one is like your scripts with argv

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#so you are defining a function, giving the function a name and 
#defining the variables that are part of your function
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" %(arg1, arg2)
	
#this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
	print "I got nothin'."
	
print_two("Jessica", "Ice")
print_two_again("Jessica", "Ice")
print_one("First!")
print_none()

#this is my functions for fun
#I'm going to concatenate vars or add them together.. like a boss
def concatenate(var1, var2, var3):
	concat = var1 + var2 + var3
	print concat
	
concatenate(1, 4, 9)
concatenate("Tom", "or", "row")
concatenate(input("Enter a number: "), input("Please enter another number: "), input("and one more.. "))

#Lets set up a function to determine how much a person makes a week
print "How much do you earn per hour?",
pay_per_hour = input("In USD please...")
print "How many hours do you work per week?",
hours_per_week = input()
def weekly_earnings(var1, var2):
	weekearn = var1 * var2
	print "You earn %r dollars per week." % weekearn

weekly_earnings(pay_per_hour, hours_per_week)

	