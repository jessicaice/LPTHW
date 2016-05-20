#Exercise 21: Functions Can Return Something
#From Learn Python the Hard Way
#Created on May 17, 2016
#Created by Jessica Ice
#Last edited on May 17, 2016

def add(a, b):
	print "ADD %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

#A puzzle for the extra credit.

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) 

print "That becomes:", what, "Can you do it by hand?"

guess = -4391

print "I think it is %d." % guess

print guess == what