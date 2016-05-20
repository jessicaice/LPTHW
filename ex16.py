#Exercise 16 from Learn Python the Hard Way
#Created by Jessica Ice
#Created on May 10, 2016
#Last Edited on May 10, 2016

#Here are some extra commands and what they do:
# close - closes the file (like file save)
# read - reads the contents of the file
# readline - reads just one line of a text file
# truncate - empties the file (careful!)
# write('stuff') - writes 'stuff' into the file

#Importing argv functions
from sys import argv

script, filename = argv

#Printing instructions for executing the script
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

#Printing how we would execute the truncation of the file
print "Opening the file..."
target = open(filename, 'w')
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to write these to the file."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

all_lines = "%s\n%s\n%s\n" % (line1, line2, line3)

#print all_lines

print "I'm going to write these to the file."

target.write(all_lines)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()

# when you open a file in a mode you can append 
#things onto it - useful for the webscraping