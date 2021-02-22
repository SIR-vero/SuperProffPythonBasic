# Take a number as INPUT (say N) and calcualte the sum of the first N numbers.
# E.g.	N = 5
#		sum = 1+2+3+4+5 = 15

N = int(input("Enter a number : "))
count = 1
sum = 0
while count <= N:
	sum = sum + count
	count = count + 1
print("The sum of 1 to ", N, " is : ", sum)
	
# count -> 1 2 3 4 5
# sum -> 6