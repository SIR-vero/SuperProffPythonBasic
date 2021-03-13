# x = 135
# 135 is div by 1, 3, 5
# x = 465
# div by 4, 6, 5

x = int(input("Enter a number: ")) 

y = str(x) # y = "102"
ans = True
for i in y:
	try:
		if x%(int(i)) != 0:
			ans = False
			break
	except Exception as e:
		print(x, "has a 0")
		ans = False
		break

if ans:
	print(x, "is special number")
else:
	print(x, "is not special number")