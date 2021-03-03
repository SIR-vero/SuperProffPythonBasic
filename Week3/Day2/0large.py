n = int(input("How many numbers you want to enter: "))
count = 1
numbers = list()
while count <= n:
	query = int(input("Enter the numbers: "))
	numbers.append(query)
	count = count + 1

m = max(numbers)
print("max is ", m)