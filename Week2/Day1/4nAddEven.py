# Take a number as INPUT (say N) and calcualte the sum of the first N even numbers.
# E.g.	N = 4
#		sum = 2+4 = 6
# E.g.	N = 5
#		sum = 2+4 = 6

N = int(input("Enter a number: "))
count = 1
sum = 0
while count <= N:
	if count%2 == 0:
		sum = sum + count
	count = count + 1
print("The sum of even numbers below ", N, " is : ", sum)