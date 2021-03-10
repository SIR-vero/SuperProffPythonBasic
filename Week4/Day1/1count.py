# Take N names in a List and count the names which starts with letter 'a'
# E.g x = ["Tarush", "Ayush", "aman", "akshay"]
# print 3

n = int(input("Enter how many names you will enter: "))
names = list()

index = 1 # 0 1 2 3	 n = 4
while index <= n:
	name = input("enter a name: ")
	names.append(name)
	index = index + 1


counts = 0

for name in names:
	
	name1 = name.lower()
	if name1[0] == 'a':
		counts = counts + 1
		print(name)
		
print ("names starting with a are : ", counts)

