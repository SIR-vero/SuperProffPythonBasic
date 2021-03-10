# Given a list of N numbers.
# print the numbers which are less than 101, in increasing order.
# eg. x = [101, 123, 100, 99, 1, 56]
# print 1, 56, 99, 100

n = int(input("Enter how many numbers you will enter: "))
num = list()

index = 1 # 0 1 2 3	 n = 4
while index <= n:
	number = int(input("enter a number: "))
	num.append(number)
	index = index + 1

ans = []
for number in num:
	if number < 101:
		ans.append(number)

ans.sort()		
print(ans)