# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same.
# 'end start equal'
# 'tenet' -> fine
# 'A'
# 'teneeeneet'
# 'aa'
# ['tenet' ,'A' ,'teneeeneet' ,'aa'] n = 4
#    0		 1			2		3

#
n = int(input("How Many string you want to enter: "))
words = list()
index = 1
while index <= n:
	word = input("Enter a word: ")
	words.append(word)
	index = index + 1

end = n-1
index = 0
while index <= end:
	if len(words[index]) >= 2 and words[index][0] == words[index][-1]:
		print(words[index], "is end-start-equal string")
	else :
		print(words[index], "is Not end-start-equal string ")
	index = index+1

