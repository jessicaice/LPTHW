#Exercise 17: More Files from Learn Python the Hard Way
#Created by Jessica Ice
#Created on May 12, 2016
#Last Edited on May 12, 2016

#cp test1.txt new_file.txt

from sys import argv
#The command exists returns "True" if a file exists and False if not
from os.path import exists

script, from_file, to_file = argv

#explains what we are going to do in the script
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()

indata = open(from_file).read()

#tells me how long the input file is
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
