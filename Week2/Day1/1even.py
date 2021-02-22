# Take an number as input (say N) and print all the EVEN numbers between 1 and N

# N = 6, 
# 1,2,3,4,5,6
N = int(input("Enter a number: "))
count = 1
while count <= N:
	if count%2 == 0:
		print(count, end=" ")
	count = count + 1

# N = 5
# count		-> 1 2
# console 	-> error 2 