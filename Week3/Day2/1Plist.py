# Given N numbers take out the prime numbers and put them in a separate list.

def check_prime(x):
	if x == 1 or x == 0:
		return False
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
			return False
		else :
			return True

n = int(input("How many numbers you want to enter: "))
count = 1
numbers = list()
while count <= n:
	query = int(input("Enter the numbers: "))
	numbers.append(query)
	count = count + 1

# numbers = [1,3,5,10]	-> 0 1 2 3
prime = []
count = 0
length = len(numbers) - 1
#length = length - 1
while count <= length:
	numbers[count]
	if check_prime(numbers[count]):
		prime.append(numbers[count])
	count = count + 1
	
print("The given numbers were ", numbers)
print("and prime numbers are ", prime)