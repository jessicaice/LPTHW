#We are now learning how to take input and feed it into programs
# Make sure to put a comma at the end of each print line. 
#This is so the print doesn't end the line with a newline character
# go to the next line
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

#Prints all the input from the variables above.
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

#I am going to create my own form about college attendance
print "Please fill in the following information:"
print "First Name",
fname = raw_input()
print "Last Name",
lname = raw_input()
print "Name of Undergraduate insitution",
college = raw_input()
#adding an if statement to add display logic to the code
if college == "Jacobs":
	print "Year of Graduation",
	grad_year = raw_input()
	print "College Major",
	major = raw_input()


print "Your name is %s %s and you went to %s University." % (
	fname, lname, college)
	