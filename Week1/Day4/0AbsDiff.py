#Given two Numbers find their Absolute Difference.
#Absolute Diff may be defined as the distance b/w two numbers on the number line

#Absolute Diff b/w -4 and 3 is -> 7
#Absolute Diff b/w  2 and 5 is -> 3

#		-5	  -4    -3    -2    -1     0     1     2     3     4     5
#	-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----
#			   |-----------------7-----------------------|
#												   |--------3--------|

# Write a program (W.A.P) that takes two numbers and gives their absolute Difference.

x = int(input("Enter first number : "))
y = int(input("Enter Second number : "))

maximum = max(x, y)
minimum = min(x, y)
abs_diff = maximum - minimum

print("The Absolute Difference is :", abs_diff)