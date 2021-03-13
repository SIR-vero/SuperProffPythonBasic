# x = 123
#ans = 6 = 1 + 2 + 3

# x = 456
# ans = 4 + 5 + 6 = 15

x = int(input("Enter a number: ")) # x = 123
y = str(x) # y = "123"
ans = 0
for i in y:
	ans = ans + int(i)

print(ans)