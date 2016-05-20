#Lesson 20: Function and Files
#From Learn Python the Hard Way
#Created by Jessica Ice
#Created on May 16, 2016
#Last edited on May 16, 2016

# This imports the file as a variable that you can type into the 
# command line
from sys import argv

# This defines that you are going to use a file as argv
script, input_file = argv

# This a is a function that prints the entire contents 
# of your document
def print_all(f):
	print f.read()

# This rewinds the file that was printed	
def rewind(f):
	f.seek(0)
	
#This prints off a single line
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file :\n"

print_all(current_file)

print "Now let's rewind, kind of a like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)