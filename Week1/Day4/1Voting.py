#	Given The age of a person determine whether he can vote or not 
#	A person whose age is greater than or equal to 18 can vote.
#	If the person can Vote , provide him with a list of 4 candidates,
#	and take his vote and display that whom he voted.

#	~~~~~~~~~~~~~~~~~~~~~~~~~~
#		CANDIDATE LIST
#	~~~~~~~~~~~~~~~~~~~~~~~~~~
#	1. Akshay
#	2. Dhruv
#	3. Aman
#	4. Sanchit

age = int(input("Enter your age : "))
if age >= 18:
	print('''You can vote: 
			candidates list :
			1. Akshay
			2. Dhruv
			3. Aman
			4. Sanchit''')
	vote = int(input("Cast your Vote (write the num.) "))
	if vote == 1:
		print("You have voted to : Akshay")
	elif vote == 2:
		print("You have voted to : Dhruv")
	elif vote == 3:
		print("You have voted to : Aman")
	elif vote == 4:
		print("You have voted to : Sanchit")
else:
	print("You can't Vote ")