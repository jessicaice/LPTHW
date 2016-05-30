#Lesson 32: Loops and Lists
#Created by Jessica Ice
#Created on May 29, 2016

#creating several lists to run through the loop
the_count = [1, 2, 3, 4, 5] 
fruits = ['apples', 'oranges', 'pears', 'apricot']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list

for number in the_count:
	print "This is count %d" %number
	
#same as above

for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
#also we can go through mixed lists too
#notice we have to use %r since we don't know what is in the list

for i in change:
	print "I got %r" %i
	
#we can also build lists, first start with an empty one

elements = []
#testing if you can skip the for loop to append things into a list
test = range(0,6)
# then us the range function to do 0 to 5 counts

for i in range(0, 6):
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)
	
for i in elements:
	print "Element was: %d" % i
	
for i in test:
	print i