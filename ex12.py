#This is the code for Lesson 12 of Learn Python the Hard Way
#Written by Jessica Ice
#Created on May 6, 2016
#Last edited on May 6, 2016

#This is code to explain a more streamlined way to 
# gather input in a form (using less lines)

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
#you can use pydoc to find information about special python commands
#to exit the help files hit q
