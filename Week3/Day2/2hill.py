# Given the heights of various points on a terrain identify if a point is hill. A hill is a point which is greater than it's adjacent points. Eg. 1 3 2	here point '3' is a hill.



#  length = 7
#  start = 1
#  end = 5

n = int(input("How many points you want to enter: "))
count = 1
numbers = list()
while count <= n:
	query = int(input("Enter the point height : "))
	numbers.append(query)
	count = count + 1
	
if n < 3:
	print("there is no hill, cant determine with less than 3 points")
else:
	hills = 0
	index = 1
	end = len(numbers) - 2

	
	while index <= end:
		#  1 3 2 5 2 7 1
		#  0 1 2 3 4 5 6
		if numbers[index - 1] < numbers[index] and numbers[index + 1] < numbers[index]:
			hills = hills + 1
		index = index + 1
	

	
	print ("the number of hills is/are ", hills)