#Exercise 42: Is-A, Has-A, Objects, and Classes
#Learn Python the Hard Way
#Created by Jessica Ice
#Created on June 26, 2016

## Animal is-a object
class Animal(object):
	pass
	
## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has-a name
		self.name = name
		
## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		##the Cat has-a name
		self.name = name			
		
## Person is-a object
class Person(object):
	
	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## Employee is-a Person
class Employee(Person):
	
	def __init__(self, name, salary):
		## Employee has-a name
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	pass
	
## Salmon is-a fish
class Salmon(Fish):
	pass
	
	
## Halibut is-a fish
class Halibut(Fish):
	pass
	

##rover is-a Dog with the name Rover

rover = Dog("Rover")

##Satan is-a Cat with the name Satan
satan = Cat("Satan")

##Mary is-a Person with the name Mary
mary = Person("Mary")

##Mary has-a pet, the pet is-a satan, the pet is-a cat
mary.pet = satan

## frank is-a employee and has-a salary of 120000
frank = Employee("Frank", 120000)

##frank has-a pet, the pet is-a dog, the dog has-a name "rover"
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()
