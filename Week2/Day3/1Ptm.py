# Given marks of Maths and Science.
# Parents are called if in any subj. marks are less than 30.

# and if marks in one subj are in between 30 and 40 (i.e 40 > marks >=30) and 
# the marks in other subj is less than 55 then parents are called 
# but if marks in second subj are greater than equal to 55 then parents are not called.

# E.g maths -> 40 Sci -> 40 then parents are NOT called
# E.g maths -> 35 Sci -> 54 then parents are CALLED
# E.g maths -> 29 Sci -> 90 then parents are CALLED
# E.g maths -> 35 Sci -> 55 then parents are NOT called

def call_or_not(maths, sci):
	if maths < 30 or sci < 30:
		return True
	elif (maths < 40 and maths >= 30 and sci < 55) or (sci < 40 and sci >= 30 and maths < 55):
		return True
	else:
		return False

maths = int(input("Enter the Math Marks : "))
sci = int(input("Enter the Science Marks : "))

x = call_or_not(maths, sci)

if x:
	print("Call your parent")
else:
	print("do not call")