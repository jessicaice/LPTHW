#Exercise 24: More practice 
#Learn Python the Hard Way
#Created by Jessica Ice
#Created on May 21, 2016
#Last edited on May 21, 2016

print "Let's practice everything."
print 'You\'d need to know \'but escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t Thelovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""
print "_________________"
print poem
print "_________________"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
  jelly_beans = started * 500
  jars = jelly_beans / 1000
  creates = jars / 100
  return jelly_beans, jars, crates
  
start_point = 10000
beans, jars, crates = secret_formula(start_point) 

print "With a starting point of: %d crates." (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." %secret_formula(start_point)
