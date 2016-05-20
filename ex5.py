#I am going to define some variables that describe myself

my_name = 'Jessica Ice'
my_age = 26 # not a lie
my_height = 62 #inches
my_weight = 164 #pounds
my_eyes = 'Hazel'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "She's %d inches tall." % my_height
print "She's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee." %my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)  

#here I rename the variables without the my in front of them	
name = 'Jessica Ice'
age = 26 # not a lie
height = 62 #inches
weight = 164 #pounds
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'
 
metric_w = 0.453592
metric_h = 2.54

weight_metric = weight * metric_w
height_metric = height * metric_h

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "Or if you are one of those weird Europeans she's %f centimeters tall." % height_metric
print "She's %d pounds heavy." % weight
print "Again - for Europeans she's %r kilos heavy." % weight_metric
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." %teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight) 