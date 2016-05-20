#Below I am defining different variables with strings in them
# and I am putting formatted variables inside the strings
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#Here I am printing some of the strings from above and some that have strings inside stirngs
print x
print y

#More examples of how to use formatted variables inside a string
print "I said: %r." % x
print "I also said: '%s'." % y

#False is actually not a string but it is placed inside a string below
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
#This demonstrates how to concatenate two strings
w = "This is the left side of..."
e = "a string with a right side."

print w + e
