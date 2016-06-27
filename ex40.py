#Exercise 40: Modules, Classes, and Objects
#From Learn Python the Hard Way
#Created by Jessica Ice
#Created on June 12, 2016

#This code will begin to explain object-oriented programming

#Modules
#Modules are code you write that include variables or functions that can be called 
#in another set of code using the module (code name) and the dot (.) operator with 
#the variable or function name

#Classes
#Class is a way you can take a grouping of functions and data and place them inside
#a container to you can access them with the dot (.) operator

#Object
# "Instantiate" is creating an object from a class. 
#This instantiation creates a mini-module which you can assign to a variable to work with

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()





