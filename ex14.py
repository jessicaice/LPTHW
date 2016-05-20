#Exercise 14 of Learn Python the Hard Way
# Created by Jessica Ice
# Created on May 8, 2016
# Last Edited on May 8, 2016

# This is going to teach us how to combine raw_input and argv

from sys import argv

script, user_name, occ = argv
prompt = 'Answer here, or else... '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me. 
You live in %r and you are a %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, occ, computer)
