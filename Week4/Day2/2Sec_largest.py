# x = [1, 56, 100, 15]
# x = [1, 15, 56, 100]
# largest = 100
# second largest = 56

n = int(input("Enter how many numbers: ")) # n = 1
numbers = list()
index = 1
while index <= n:
	x = int(input("Enter a number: "))
	numbers.append(x)
	index = index + 1
	
numbers.sort()
if n > 1:
	ans = numbers[-2]
	print("the second largest element is ", ans)
else:
	print("second largest element is not possible with one or zero element")