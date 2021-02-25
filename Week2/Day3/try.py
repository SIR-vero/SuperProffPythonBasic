def hello(x):
	x = x+10
	if x <= 100:
		print("not yet ")
	else :
		print("hurray !")

while True:
	score = int(input("Enter : "))
	hello(score)
	if score > 100:
		break