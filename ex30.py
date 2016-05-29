#Exercise 30: Else and If
#Learn Python the Hard Way
#Created by Jessica Ice
#Created on May 29, 2016

#define the parameters
people = 30
cars = 40
trucks = 15

#compares the number of cars and people
if cars > people: 
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."
	
#compares the number of trucks and cars
if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

#Comparing the number of trucks and people	
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."
	
