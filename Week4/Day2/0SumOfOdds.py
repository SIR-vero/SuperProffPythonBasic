# x = [1, 56, 8, 9, 11]
# ans = 21 = 1+9+11

n = int(input("Enter how many numbers: "))
index = 1
numbers = []
while index <= n:
	x = int(input("Enter a number: "))
	numbers.append(x)
	index = index + 1

ans = 0
for num in numbers:
	if num%2 == 1:
		ans = ans + num
print("the sum of odd numbers are ", ans)