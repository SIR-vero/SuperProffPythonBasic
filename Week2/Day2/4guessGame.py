# Create a random number using random module.
# ask the User to guess that number.
# give the user 10 tries.

import random
random_num = random.randint(1, 100)

#print("ran num: ", random_num)

print("we have a random number between 1-100 guess that number")
print("(you have 10 tries)")

count = 1
while count <= 10:
	x = int(input("What's your guess: "))
	if x == random_num:
		print("you guessed correct! ")
		break
	else :
		print("WRONG, you have ", 10-count, " tries left")
		if random_num < x:
			print("go a little lower !")
		else:
			print("go a little higher !")
	count = count + 1
if x == random_num:
	print("Congrats ! ")
else:
	print("no tries left the number was ", random_num)


