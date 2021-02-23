# Ask the user to input a number (say N)
# Then print a right triangle of height N.

# E.G. N = 5

#	*
#	**
#	***
#	****
#	*****

from art import *
n = int(input("Height of triangle: "))
count = 1
tprint("hello")
while count <= n:
	tprint(count * "*")
	count = count + 1


