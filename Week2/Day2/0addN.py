# Ask user how many numbers he want to add (say N).
# Input N numbers and print their Sum.

# E.G.	User Enters N = 5
# 1st number = 3
# 2nd number = 4
# 3rd number = 2
# 4th number = 2
# 5th number = 5

# The sum is 16

n = int(input("How many numbers you want to add: "))
sum = 0
count = 1
while count <= n:
	print("Enter the ", count, " number: ")
	x = int(input())
	sum = sum + x
	count = count + 1
print("the sum is ", sum)


