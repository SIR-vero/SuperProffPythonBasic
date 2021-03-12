n = int(input("How Many string you want to enter: "))
words = list()
index = 1
for index in range(1, n+1):
	word = input("Enter a word: ")
	words.append(word)
	#index = index + 1
	
end = n-1
index = 0
# [aaa, bab, cad, ccc] n = 4
#   0    1    2    3

# 'aaa'
#  012
similar = list()
for index in range(0, n):
	count_of_first_char = words[index].count(words[index][0])
	lenght = len(words[index])
	if lenght == count_of_first_char:
		#print(words[index], " have all similar char")
		similar.append(words[index])
	else:
		print(words[index], " does not have all similar char")
	
	
print ("similar words are ", similar)