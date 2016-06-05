#Exercise 38: Doing Things to Lists
#Learn Python the Hard Way
#Created by Jessica Ice
#Created on June 5th

#This is code to help me understand what is going on when python interacts with lists
# and how python executes functions and interacts with variables and arguments

#Important to note - difference between an argument and a variable/parameter

# Variable/Parameter is the definition of some set of valuables or data that is possible to change
# Argument is the actual data that you pass into the method's variable/parameter

#This is the original list of things
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

#Here is how I split the list apart into elements
stuff = ten_things.split(' ')
#This is an addition list of elements that I can add to "ten_things"
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#This while loop allow me to append each of the elements onto the list as long as the 
#list has 10 or less elements.
while len(stuff) !=10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

#This prints the final list
print "There we go: ", stuff

print "Let's do some things with stuff."

#This prints the second word in the list
print stuff[1]
#This prints the last element of the list
print stuff[-1]
#This pops off the last element in the list and prints it
print stuff.pop()
#This removes the split we previously made in the list and rejoins the elements
print ' '.join(stuff)
#This prints the items in the list with a # in between them 
#but it only prints items in the list that start at the first number inside the bracket 
#and stop before the second number inside the bracket. 
print '#'.join(stuff[3:5])
