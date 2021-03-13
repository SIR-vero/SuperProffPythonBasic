import random

msg = input("enter message: ")
msg = msg.lower()

rand = (random.choices('abcdefghijklmnopqrstuv', k = len(msg)))

for i in range(0, len(msg)):
	rand.insert(i*2, msg[i])
	
print(''.join(rand))