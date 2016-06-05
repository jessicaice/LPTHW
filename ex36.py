#Exercise 36: Designing and Debugging
#From Learn Python the Hard Way
#Created by Jessica Ice
#Created on June 1, 2016

#This is a set of code to create my own text based adventure game
# My text based adventure game is going to be based on my life
#I am going to go through the stages of life and have different options to
#stay where you are, run away, travel, take jobs, become rich and famous, or 
#save the world. It will follow the structure below

#Born
# You are born and you choose to stay where you are or run away
# If you stay where you are you die of dispair 
# if you run away you end up in Europe

#Europe
# If you end up in Europe you will either get drafted to the circus, go to school, 
#or become a snowboarding instructor

#Circus
#You can either choose to go to Romania or France.
#If you go to Romania you become a Roma.
#No one ever hears from you again.
#If you go to France you become a mime.
#People see you, but no one ever hears from you again.


#School
#You can either choose to major in politics, computer science, or under water basket weaving.
# If you major in politics you move to DC and go to grad school at Georgetown.
# You are recruited to work for the state department and write a bunch of emails to Hillary Clinton
# You end up spending the rest of your life in Federal prison.


#If you major in computer science you can choose to work for Google, move to Cleveland.
#If you work for google you end up building a nest below your desk and never leave the campus again.
# If you move to Cleveland a bunch of people ask you why you moved there.
#Why did you move there?


#Cleveland
# If you moved for the money you work for KeyBank and do CCAR modeling. 
# You live #KeyBankLife and buy lots of bottles. 
# Eventually the black hole in your heart eats away at you and you waste into nothing.

#NEED TO FINISH THIS
# If you moved for love you get married.
# You have lots of babies. You are happy, except for all the vomit.
# You still lose because you have to pay for college for all those kids.

# If you moved "Cuz" - you start your own business, fall in love, and just win.
# You win.

#NEED TO FINISH THIS
# Snowboard Instructor
# If you become a snowboarding instructor you will get paid a lot of money
# You can either spend it on a surf vacation or invest in a retirement account.
# If you invest in surf trip you met a really hot surfer and fall in love.
# You die with a heart full of love but completely penniless.
# If you invest you become rich and end up living on the Gold Coast of Switzerland.
# You are neighbors with Roger Federer. 
# Still you never find love and die alone. 

#This code explains the circus option after the european option.
def circus():
	print "Where will you join the circus?"
#This is the code that lists your options
	circusops = ["1. Romania", "2. France"]
#This displays your options on separate lines to the reader.
	print '\n'.join(circusops), '? '
	circuschoice = raw_input('> ')
	
	if circuschoice == "1":
		print "You become a Roma."
		dead("No one ever hears from you again.")
	elif circuschoice == "2":
		print "You become a mime."
		dead("People see you, but no one ever hears from you again.")
	#This code ensures that the reader types in one of the numbers from above
	#If they do not they will have to restart the loop.
	else:
		print "You should have picked one of the numbers. Try again"
		circus()

#This code explains the moving to Cleveland options after choosing to major in computer science."
def cleveland():
	print "Thats cool brah."
	print "What.. why did you move to Cleveland?"
	clevelandops = ["1. For the money", "2. For love", "3. Cuz"]
	print '\n'.join(clevelandops), '? '
	clevelandchoice = raw_input('> ')
	
	if clevelandchoice == "1":
		print "Nice, you work at Key Bank."
		print "You buy a lot of bottle service and use the hashtag 'KeyBankLyfe' a lot."
		dead("Eventually the black hole in your soul eats away at you and you fade into nothing.")
	elif clevelandchoice == "2":
		print "You find true love and get married."
		print "You have lots of babies. You are happy, except for all the vomit."
		dead("You have to pay for college for all those kids.")
	#This is the only way to actually win.
	elif clevelandchoice == "3":
		print "You start your own business and fall in love."
		print "Your life is awesome. You win!"
		exit(0)
	else:
		print "Seriously - you still don't know to pick a number?"
		print "Try again!"
		cleveland()

#This code explains the options if you choose to major in computer science
# after you to go to school once you are in europe.
def computerscience():
	print "You can actually get a real job. Congratulations!"
	print "Where do you work?"
	jobops = ["1. At google", "2. In Cleveland"]
	print '\n'.join(jobops), '? '
	jobchoice = raw_input('> ')
	
	if jobchoice == "1":
		print "That's awesome... except you spend a lot of time at work."
		print "No, I mean A LOT of time.. really... A LOT."
		print "You end up building a nest below your desk on the google campus."
		dead("You become part of the matrix.")
	elif jobchoice == "2":
		cleveland()
	else:
		"You should have picked a number! Try again."
		computerscience()

#This code explains your options if you choose to go to school after you have gone to europe.
def school():
	print "What major will you pick?"
	majorops = ["1. Politics", "2. Computer Science", "3. Underwater Basket Weaving"]
	print '\n'.join(majorops), '? '
	majorchoice = raw_input('> ')
	
	if majorchoice == "1":
		print "You move to D.C. and go to grad school at Georgetown."
		print "You are recruited to work for the state department."
		print "You end up writing a bunch of emails to Hillary Clinton."
		dead("You spend the rest of your life in federal prison.")
	elif majorchoice == "2":
		computerscience()
	elif majorchoice == "3":
		print "You turn out to be a Youtube sensation."
		print "Unfortunately you didn't take your advanced scuba class as seriously"
		print "as you should have!"
		dead("You drown.")
	else:
		print "You should have picked one of the numbers. Try again!"
		school()

#This code explains your options if you choose to be a snowboard instructor after you end
#up in europe.	
def snowboard():
	print "You are going to make a lot of money."
	print "What are you going to do with all that money?"
	snowboardops = ["1. Spend it on a surf vacation", "2. Put it in an investment account"]
	print '\n '.join(snowboardops), '? '
	snowboardchoice = raw_input('> ')
	
	if snowboardchoice == "1":
		print "You meet a really hot surfer and fall in love."
		dead("You die with a heart full of love, but completely penniless")
	elif snowboardchoice == "2":
		print "You become rich and end up living on the Gold Coast in Zurich."
		print "You are neighbors with Roger Federer."
		dead("You never find love and die alone.")
	else:
		print "You should have picked one of the numbers. Try again!"
		snowboard()

#This code explains your options if you run away from home.
def europe():
	print "You end up in Europe, you are not really sure where. What do you do?"
	europeops = ["1.Join the Circus", "2.Go to school", "3.Become a snowboard instructor"]
	print '\n'.join(europeops), '? '
	europechoice = raw_input('> ')
	
	if europechoice == "1":
		circus()
	elif europechoice == "2":
		school()
	elif europechoice == "3":
		snowboard()
	else:
		print "You should have picked one of the numbers. Try again!"
		europe()

#This is the starting point of your text based adventure game.
def born():
	okoptions = ["1. Run Away", "2. Stay put and see how it works out"]
	print "You are born in Oklahoma."
	print "What do you do?"
	print "Type in the number of the choice below" 
	print '\n'.join(okoptions), '? '
	okchoice = raw_input('> ')
	
	if okchoice == "1":
		europe()
	elif okchoice == "2":
		print "Your soul withers away from the insurmontable social pressures and bigotry."
		dead("You die a sad death and no one remembers you.")
	else:
		print "You should have picked one of the numbers. Try again"
		born()
	
def dead(why):
	print why, "You lose."
	exit(0)

born()