# x = "AsdsdfVFsdf"
#xx = "aSDSDFvfSDF"

x = input("Enter a string: ")

ans = ""
for letter in x:
	if letter.isupper():
		ans = ans + letter.lower()
	else:
		ans = ans + letter.upper()

print(ans)