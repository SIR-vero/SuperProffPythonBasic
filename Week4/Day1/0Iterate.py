# Take N names in a List and print it in reverse order.
# E.g x = ["Tarush", "Anshuman", "Aman"]
# prnt -> Aman, Anshuman, Tarush

n = int(input("Enter how many names you will enter: "))
names = list()

index = 1 # 0 1 2 3	 n = 4
while index <= n:
	name = input("enter a name: ")
	names.append(name)
	index = index + 1


names.reverse()
for name in names:
	print(name, end=", ")