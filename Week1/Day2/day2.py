x = input("Enter first number ")
y = input("Enter second number ")
x = int(x)
y = int(y)

if x%y == 0:
	z = x/y
	print(x, "is divisible by", y, " and the quotient is ", z)
else:
	print(x, "is not divisible by ", y)


