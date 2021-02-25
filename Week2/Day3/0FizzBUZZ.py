# take a input and check for FIZZ buzz in that range
# check if x is div by 3 then print "FIZZ"
# check if x is div by 5 then print "buzz"
# check if x is div by 15 then print "FIZZbuzz"
# if not div by 3, 5, 15 then just print the number

# E.G. N = 15
# 1, 2, FIZZ, 4, buzz, FIZZ, 7, 8, FIZZ, buzz, 11, FIZZ, 13, 14, FIZZbuzz

def fizz_buzz(count):
	if count%15 == 0:
		return "FIZZbuzz"
	elif count%5 == 0:
		return "buzz"
	elif count%3 == 0:
		return "FIZZ"
	else :
		return count


n = int(input("Enter the range: "))
count = 1
while count <= n:
	x = fizz_buzz(count)
	print(x)
	count = count + 1






