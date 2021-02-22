# x
# check if x is div by 3 then print "FIZZ"

# check if x is div by 5 then print "buzz"

# check if x is div by 15 then print "FIZZbuzz"

# if not div by 3, 5, 15 then just print

x = input("Enter a number ")
x = int(x)
if x%15 == 0:
	print("FIZZbuzz")
elif x%5 == 0:
	print("buzz")
elif x%3 == 0:
	print("FIZZ")
else:
	print(x)

