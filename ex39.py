#Exercise 39: Dictionaries
#Learn Python the Hard Way
#Created by Jessica Ice
#Created on June 7, 2016

#This file will create a set of several dictionaries

#create a mapping of states to abbreviations

states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}
	
#create a basic set of states and some cities in them

cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some of the cities

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some of the states
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation

print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
#print every city in a state

print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" %(abbrev, city)
		
#now do both
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
#safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."
	
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city

	