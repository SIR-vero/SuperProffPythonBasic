# prime numbers div by 1 and themselves.
# 10 -> Div by 2, 5
# 7  -> Div by 1, 7
# 21 -> 1, 21, 
# 21 -> 2, 3, 4, 5, 7....., 20

def check_prime(x):
	if x == 1 or x == 0:
		print(x, "is not a prime number")
	else:
		count = 2
		p = x-1
		prime = True
		while count <= p:
			if x % count == 0:
				prime = False
				break
			count = count + 1
		if prime == False:
			print(x, "is not a prime number")
		else :
			print(x, "is a prime number")


x = int(input("Enter a number: "))
check_prime(x)