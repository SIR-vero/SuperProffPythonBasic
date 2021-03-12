# num = 20
# factors = 1, 2, 4, 5, 10, 20
# 1, 2, 3, 4, 5, ......  ,19

num = int(input("Enter the number: "))
factors = list()
for fact in range(1, num+1):
	if num%fact == 0:
		factors.append(fact)
		
print("the factors of", num,"are,", factors)