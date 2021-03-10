n = int(input("How many words: "))
words = list()

index = 1
while index <= n:
	x = input("Enter a word : ")
	words.append(x)
	index = index + 1
	
# [aeiouzab, abcdeiou, aei, mnop] n = 4
#      0         1      2    3

index = 0
end = n - 1
ans = list()

while index <= end:
	word = words[index].lower()
	v = word.count('a')
	v += word.count('e')
	v += word.count('i')
	v += word.count('o')
	v += word.count('u')
	if v >= 5:
		ans.append(word)
	index = index + 1
	
print("the words with vowels greater than or equals to 5 are ", ans)