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

# If you moved for love you get married.
# You have lots of babies. You are happy, except for all the vomit.
# You still lose because you have to pay for college for all those kids.

# If you moved "Cuz" - you start your own business, fall in love, and just win.
# You win.


# Snowboard Instructor
# If you become a snowboarding instructor you will get paid a lot of money
# You can either spend it on a surf vacation or invest in a retirement account.
# If you invest in surf trip you met a really hot surfer and fall in love.
# You die with a heart full of love but completely penniless.
# If you invest you become rich and end up living on the Gold Coast of Switzerland.
# You are neighbors with Roger Federer. 
# Still you never find love and die alone. 


def circus()
	print "Where will you join the circus?"
	circusops = ["1. Romania", "2. France"]
	print '\n'.join(circusops), '? '
	circuschoice = raw_input('> ')
	
	if circuschoice == "1":
		print "You become a Roma."
		dead("No one ever hears from you again.")
	elif circuschoice == "2":
		print "You become a mime."
		dead("People see you, but no one ever hears from you again.")
	else:
		print "You should have picked one of the numbers. Try again"
		circus()

def computerscience():
	print "You can actually get a real job. Congratulations!"
	print "Where do you work?"

def school():
	print "What major will you pick?"
	majorops = ["1. Politics", "2. Computer Science", "3. Underwater Basket Weaving"]
	print '\n'.join(majorops), '? '
	majorchoice = raw_input('> ')
	
	if majorchoice == "1":
		print "You move to D.C. and go to grad school at Georgetown."
		print "You are recruited to work for the state department. \n You end up writing, \\\
		a bunch of emails to Hillary Clinton."
		dead("You spend the rest of your life in federal prison.")
	elif majorchoice == "2":
		computerscience()
	elif majorchoice == "3":
		print "You turn out to be a Youtube sensation."
		print "Unfortunately you didn't take your advanced scuba class as seriously \\\
		as you should have!"
		dead("You drown.")
	else:
		print "You should have picked one of the numbers. Try again!"
		school()
	
def snowboard():
	print "You are going to make a lot of money."
	print "What are you going to do with all that money?"


def europe():
	print "You end up in Europe, you are really sure where. What do you do?"
	europeops = ["1. Join the Circus", "2.Go to school", "3.Become a snowboard instructor"]
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
	print why, "You loose."
	exit(0)
	 
born()