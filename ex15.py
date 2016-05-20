#This is Exercise 15 from Learn Python the Hard Way
#Created by Jessica Ice
#Created on May 9, 2016
#Edited on May 9, 2016

from sys import argv

#calling in a file name into the argv script to be opened
script, filename = argv
# I am defining a variable with information from a file
txt = open(filename)

#I am printing the name of the file
print "Here's your file %r:" % filename
#Printing the contents of the file with the command .read
print txt.read()
txt = close(filename)

#Now I am going to do the same thing as above, but input the file name
#while I am running the script
print "Type the filename again."
#Allows me to define a file I want to open
file_again = raw_input("> ")
#Allows me to create the file as a variable that I can do things with
txt_again = open(file_again)
#Allows me to open the file with the command behind the dot
print txt_again.read()
txt_again = close(file_again)
