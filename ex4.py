#number of cars available
cars = 100
#number of passengers a car can hold
space_in_a_car = 4.0
#number of current drivers of cars
drivers = 30
#number of total passengers needed to be driven
passengers = 90
#calculation of the number of cars not driven because of no driver
cars_not_driven = cars - drivers
#Number of cars driven will equal the number of drivers available to drive them
cars_driven = drivers
#total amount of passengers that can be driven in a day
carpool_capacity = cars_driven * space_in_a_car
#Average number of people that would need to go in each car
average_passengers_per_car = passengers / cars_driven

#Text to explain our cars, drivers, and passenger constraints
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#my calculation for fun
jess_birth_year = 1989
mom_birth_year = 1963
eugene_age = 31
current_year = 2016

jess_age = current_year - jess_birth_year
mom_age = current_year - mom_birth_year
eugene_birth_year = current_year - eugene_age

print "Jessica is", jess_age, "years old."
print "Kathy is", mom_age, "years old."
print "Eugene was born in", eugene_birth_year, "and is", eugene_age, "years old."
print "Mom is younger than Jessica.", mom_age < jess_age
print "Eugene is older than Jessica.", eugene_birth_year < jess_birth_year
