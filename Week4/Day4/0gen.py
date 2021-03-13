import random

# encoded_msg = "asdsdfHdfsdEsdjnsdfLasdasLasdasdOasadasd"

msg = input("enter message: ")
msg = msg.upper()

encoded_msg = ""
for i in range(0, len(msg)):
	length = random.randint(1,5) # 2
	rand = ''.join(random.choices('abcdefghijklmnopqrstuv', k = length))
	encoded_msg += rand
	encoded_msg += msg[i]
	
length = random.randint(1,5)
rand = ''.join(random.choices('abcdefghijklmnopqrstuv', k = length))
encoded_msg += rand
print(encoded_msg)