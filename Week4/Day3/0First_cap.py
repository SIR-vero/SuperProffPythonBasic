# x = "achdfAchidF"
# ans = 'A'

x = input("Enter a word: ")
ans = ""
for letter in x:
	if letter.isupper():
		ans = letter
		break

print("the first capital letter is, ", ans)