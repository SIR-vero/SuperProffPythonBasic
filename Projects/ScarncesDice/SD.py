import random
import os
import time

def draw_dice(x):
	if x == 1:
		print("+-----+")
		print("|     |")
		print("|  0  |")
		print("|     |")
		print("+-----+")
	
	elif x == 2:
		print("+-----+")
		print("|     |")
		print("| 0 0 |")
		print("|     |")
		print("+-----+")
		
	elif x == 3:
		print("+-----+")
		print("|     |")
		print("|0 0 0|")
		print("|     |")
		print("+-----+")
		
	elif x == 4:
		print("+-----+")
		print("| 0 0 |")
		print("|     |")
		print("| 0 0 |")
		print("+-----+")
		
	elif x == 5:
		print("+-----+")
		print("| 0 0 |")
		print("|  0  |")
		print("| 0 0 |")
		print("+-----+")
		
	elif x == 6:
		print("+-----+")
		print("|0 0 0|")
		print("|     |")
		print("|0 0 0|")
		print("+-----+")


def roll_dice():
	number = random.randint(1, 6) 	#1 - 6
	return number


def animate_dice(x):
	roll = random.choices('123456', k = 5)
	for i in roll:
		draw_dice(int(i))
		print("rolling....	")
		time.sleep(0.3)
		os.system('cls')
	draw_dice(x)
	print("You rolled a", x)
	

def validate(x):
	try :
		x = int(x)
	except Exception as e:
		return False
	
	if x == 0 or x == 1:
		return True
	
	return False


def game_input(moves, player1, player2):
	if moves % 2 == 1:
		print(player1, "your turn (press 0:- to roll Dice or press 1:- to pass your turn )")
		x = input()
		while validate(x) == False:
			x = input("\aplease enter 0 or 1: ")
		
		x = int(x)
		
		if x == 1:
			return 0
		else:
			dice_number = roll_dice()
			animate_dice(dice_number)
			return dice_number
		
	else :
		print(player2, "your turn (press 0:- to roll Dice or press 1:- to pass your turn )")
		x = input()
		while validate(x) == False:
			x = input("\aplease enter 0 or 1: ")
		
		if x == 1:
			return 0
		else:
			dice_number = roll_dice()
			animate_dice(dice_number)
			return dice_number

#	p1 = 0
#	p2 = 0
#	player has to reach a score of 30
#	at every turn a player has two choices
# 	roll dice or Pass
# 	if he rolls dice and get a 1. then his score reset to zero.

player1 = input("Enter your name: ")
player2 = input("Enter your friend's name: ")
max_score = int(input("Enter the max game score: "))

player1_score = 0
player2_score = 0

who_starts = random.randint(0,1)

if who_starts == 0:
	print(player1, "will start")
else :
	print(player2, "will start")
	player1, player2 = player2, player1

moves = 1
while player1_score < max_score and player2_score < max_score:
	rolled_number = game_input(moves, player1, player2)
	if rolled_number == 0:
		if moves % 2 == 1:
			print(player1, " passed")
		else:
			print(player2, " passed")
	else:
		if moves % 2 == 1:
			if rolled_number == 1:
				player1_score = 0
				print(player1, "rolled a one hence score has been set to zero ")
			else:
				player1_score = player1_score + rolled_number
		else:
			if rolled_number == 1:
				player2_score = 0
				print(player2, "rolled a one hence score has been set to zero ")
			else:
				player2_score = player2_score + rolled_number
	
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t", player1, "score: ", player1_score)
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t", player2, "score: ", player2_score)
	
	#os.system('cls')
	
	moves = moves + 1
	

if player1_score >= max_score:
	print(player1, "WON!!")
else :
	print(player2, "WON!!")
