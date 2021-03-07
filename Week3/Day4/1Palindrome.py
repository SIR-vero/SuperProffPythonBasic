#	Given a string determine whether it is a PALINDROME or not. A palindrome is a string whose reverse is same as the original string. E.g. "tenet" is a palindrome, "tarush" is not a palindrome.



while True:
	str = input("Enter the word (to end enter 'quit'): ")
	str = str.lower()
	print(str)
	if str == 'quit':
		break
	liststr = list(str)
	liststrC = liststr.copy()
	liststr.reverse()
	
	if liststrC == liststr:
		print("PALINDROME!")
	else :
		print("Not PALINDROME!")
