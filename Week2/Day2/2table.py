# Ask the user to input a number.
# Then print its multiplication table upto 10.

# E.G. N = 5
# then print

# 5 * 1  =  5
# 5 * 2  = 10
# 5 * 3  = 15
# 5 * 4  = 20
# 5 * 5  = 25
# 5 * 6  = 30
# 5 * 7  = 35
# 5 * 8  = 40
# 5 * 9  = 45
# 5 * 10 = 50

n = int(input("Enter the number whose table you want: "))
count = 1
while count <= 10:
	print(n, "*",count, " = ", n*count)
	count = count + 1
