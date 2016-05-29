#Exercise 31: Making Decision
#Learn Python the Hard Way
#Created by Jessica Ice
#Created on May 29th

#Starting my test based adventure game with a question
print "You enter a dark room with two doors. Do you go through door \
1 or door 2?"

#creating answers to my question
doors = ['1', '2']

#Creating the input mechanism for my question
door = raw_input(' or '.join(doors) + '? ')

if door == "1":
	print "There's a giant bear here eating a cheese cake \
	What do you do?"

	#Creating the options for door number 1	
	door1opt = ['Take the cake.', 'Scream at the bear.']

	#Ability to put in the options for door number 1
	bear = raw_input(' or '.join(door1opt) + '? ')

	if bear == 'Take the cake':
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats you legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away!" % bear
	
elif door == "2":
	print "You start into the endless abyss at Cthulhu's retina."

	door2opt = ['Blueberries', 'Yellow jacket clothespins', 
		'Understanding revolvers yelling melodies']
	
	insanity = raw_input(' or '.join(door2opt) + '? ')

	if insanity == 'Blueberries' or insanity == 'Yellow jacket clothespins':
		print "Your body survives powered by a mind of jello.\
		Good job!"
		
	else:
		print "The insanity rots your eyes into a pool of muck.\
		Good job!"
		
else:
	print "You just lose brah."