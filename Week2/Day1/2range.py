# Take an number as input (say N) and check if its between 100 and 150(inclusive) if not then again ask for input, keep repeating until
# the num is between 100 and 150.

N = int(input("Enter a number: "))
if N > 100 and N < 150:
	print("Correct !! ")
else:
	while N < 100 or N > 150:
		N = int(input("Enter a number: "))
	print("Correct !! ")
	

#N = int(input("Enter a number: "))
#while N < 100 or N > 150:
#	N = int(input("Enter a number: "))
#print("correct !! ")