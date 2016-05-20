#Exercise 13 of Learn Python the Hard Way
#Exercise on Parameters, Unpacking, Variables
#Created by Jessica Ice
#Created on May 6, 2016
#Last edited on May 6, 2016

#going to learn how to import arguments into python

#This is an import line - this is how I add modules to my script
# argv is an "argument variable" 
from sys import argv

#This unpacks the arguments  - gets assigned to variables 
script, undergrad, gradschool = argv


print "The script is called:", script
print "You went to this undergraduate school:", undergrad
print "You went to this graduate school:", gradschool
best_school = raw_input("Which of the schools do you think is best?" )

print "Do you think %r is best?" % undergrad,
print best_school == undergrad
print "Do you think %s is best?" % gradschool,
print best_school == gradschool

#from sys import argv
#script, first, second, third = argv
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is", second
# print "Your third variable is:", third

