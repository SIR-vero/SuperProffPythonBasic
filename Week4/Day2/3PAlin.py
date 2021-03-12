# x ["tenet", "tarush", "racecar"]
# palin = ["tenet", "racecar"]

def check_palindrome(word):
	word = word.lower()
	listword = list(word)
	listwordC = listword.copy()
	listword.reverse()
	if listword == listwordC:
		return True
	else:
		return False


n = int(input("Enter how many strings: "))
index = 1
words = []
while index <= n:
	x = input("Enter a word: ")
	words.append(x)
	index = index + 1

palindromes = []
for word in words:
	if check_palindrome(word):
		palindromes.append(word)

print("the palindromic strings are : ", palindromes)
	
	
	
	