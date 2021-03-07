n = int(input("How many numbers"))
index = 1
numbers = list()
while index <= n:
	x = int(input("enter the number "))
	numbers.append(x)
	index = index + 1

end = n-2
index = 0
# 1 2 3 4 50 90
# 0 1 2 3 4  5
# n = 6
# end = 6-2 = 4

# 1 2 3 3 2 5 10
# 0 1 2 3 4 5 6
isInc = True
while index <= end:
	if numbers[index] >= numbers[index + 1]:
		isInc = False
		break
	index = index + 1

if isInc:
	print("the sequence is Strictly increasing")
else:
	print("the sequence is not Strictly increasing")