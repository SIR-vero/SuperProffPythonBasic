import os
import time
import random
# a | b | 02 
#---+---+---
# d | 11 | f
#---+---+---
# 20 | h | 22 

in_put = [["a", "b", "c"],["d", "e", "f"],["g", "h", "i"]]

def draw_board(in_put):	
	os.system('cls')
	
	print(" ",in_put[0][0]," | ",in_put[0][1]," | ",in_put[0][2],sep = "")
	print("---+---+---")
	print(" ",in_put[1][0]," | ",in_put[1][1]," | ",in_put[1][2],sep = "")
	print("---+---+---")
	print(" ",in_put[2][0]," | ",in_put[2][1]," | ",in_put[2][2],sep = "")
	
def validate(x, in_put):
	if x == 'a' and in_put[0][0] == 'a':
		return True
	elif x == 'b' and in_put[0][1] == 'b':
		return True
	elif x == 'c' and in_put[0][2] == "c":
		return True
	elif x == 'd' and in_put[1][0] == "d":
		return True
	elif x == 'e' and in_put[1][1] == "e":
		return True
	elif x == 'f' and in_put[1][2] == "f":
		return True
	elif x == 'g' and in_put[2][0] == "g":
		return True
	elif x == 'h' and in_put[2][1] == "h":
		return True
	elif x == 'i' and in_put[2][2] == "i":
		return True
		
	return False
		

def game_input(moves, player1, player2, player1_sym, player2_sym):
	if moves % 2 == 1:
		draw_board(in_put)
		print(player1, '(', player1_sym, ')', "  your turn ")
		x = input("Enter a valid position: ")
		x = x.lower()
		while validate(x, in_put) == False:
			draw_board(in_put)
			print(player1, '(', player1_sym, ')', "\aPlease enter a valid position: ")
			x = input()
			x = x.lower()
		if x == 'a':
			in_put[0][0] = player1_sym
		elif x == 'b':
			in_put[0][1] = player1_sym
		elif x == 'c':
			in_put[0][2] = player1_sym
		elif x == 'd':
			in_put[1][0] = player1_sym
		elif x == 'e':
			in_put[1][1] = player1_sym
		elif x == 'f':
			in_put[1][2] = player1_sym
		elif x == 'g':
			in_put[2][0] = player1_sym
		elif x == 'h':
			in_put[2][1] = player1_sym
		elif x == 'i':
			in_put[2][2] = player1_sym
	else :
		draw_board(in_put)
		print(player2, '(', player2_sym, ')', "  your turn ")
		x = input("Enter a valid position: ")
		x = x.lower()
		while validate(x, in_put) == False:
			draw_board(in_put)
			print(player2, '(', player2_sym, ')', "\aPlease enter a valid position: ")
			x = input()
			x = x.lower()
		if x == 'a':
			in_put[0][0] = player2_sym
		elif x == 'b':
			in_put[0][1] = player2_sym
		elif x == 'c':
			in_put[0][2] = player2_sym
		elif x == 'd':
			in_put[1][0] = player2_sym
		elif x == 'e':
			in_put[1][1] = player2_sym
		elif x == 'f':
			in_put[1][2] = player2_sym
		elif x == 'g':
			in_put[2][0] = player2_sym
		elif x == 'h':
			in_put[2][1] = player2_sym
		elif x == 'i':
			in_put[2][2] = player2_sym
		

def check_win(in_put):
	if in_put[0][0] == player1_sym and in_put[0][1] == player1_sym and in_put[0][2] == player1_sym:
		return 1
	elif in_put[0][0] == player2_sym and in_put[0][1] == player2_sym and in_put[0][2] == player2_sym:
		return 2
	
	if in_put[1][0] == player1_sym and in_put[1][1] == player1_sym and in_put[1][2] == player1_sym:
		return 1
	elif in_put[1][0] == player2_sym and in_put[1][1] == player2_sym and in_put[1][2] == player2_sym:
		return 2
	
	if in_put[2][0] == player1_sym and in_put[2][1] == player1_sym and in_put[2][2] == player1_sym:
		return 1
	elif in_put[2][0] == player2_sym and in_put[2][1] == player2_sym and in_put[2][2] == player2_sym:
		return 2 
	
	if in_put[0][0] == player1_sym and in_put[1][0] == player1_sym and in_put[2][0] == player1_sym:
		return 1
	elif in_put[0][0] == player2_sym and in_put[1][0] == player2_sym and in_put[2][0] == player2_sym:
		return 2 
	
	if in_put[0][1] == player1_sym and in_put[1][1] == player1_sym and in_put[2][1] == player1_sym:
		return 1
	elif in_put[0][1] == player2_sym and in_put[1][1] == player2_sym and in_put[2][1] == player2_sym:
		return 2 
	
	if in_put[0][2] == player1_sym and in_put[1][2] == player1_sym and in_put[2][2] == player1_sym:
		return 1
	elif in_put[0][2] == player2_sym and in_put[1][2] == player2_sym and in_put[2][2] == player2_sym:
		return 2 
	
	if in_put[0][0] == player1_sym and in_put[1][1] == player1_sym and in_put[2][2] == player1_sym:
		return 1
	elif in_put[0][0] == player2_sym and in_put[1][1] == player2_sym and in_put[2][2] == player2_sym:
		return 2 
	
	if in_put[0][2] == player1_sym and in_put[1][1] == player1_sym and in_put[2][0] == player1_sym:
		return 1
	elif in_put[0][2] == player2_sym and in_put[1][1] == player2_sym and in_put[2][0] == player2_sym:
		return 2
		
	return 0

player1 = input("Enter your name: ") # p1 = "Ayush"
player2 = input("Enter your Friend's name: ")

assigned_symbol = random.randint(0, 1) # 0, 1

player1_sym = ""
player2_sym = ""

if assigned_symbol == 0:
	print(player1, "is 'X'")
	print(player2, "is 'O'")
	player1_sym = "X"
	player2_sym = "O"
	
else :
	print(player1, "is 'O'")
	print(player2, "is 'X'")
	player1_sym = "O"
	player2_sym = "X"

who_starts = random.randint(0, 1) # 0, 1

if who_starts == 0:
	print(player1, "will start")
else :
	print(player2, "will start")
	player1, player2 = player2, player1
	player1_sym, player2_sym = player2_sym, player1_sym
	
time.sleep(5)


moves = 1
while moves <= 9:
	game_input(moves, player1, player2, player1_sym, player2_sym)
	draw_board(in_put)
	check = check_win(in_put)
	if check == 1:
		print(player1, "WON!!!")
		break
	elif check == 2:
		print(player2, "WON!!!")
		break
	elif moves == 9:
		print("DRAW!!!")
		break
	moves = moves + 1
	




# moves = 1, 2, 3, 4, 5
# who_starts = 0
# every odd move p1
# p1 | p2 | p1 
#--- +--- +---
# 	 |	  |	
#--- +--- +---
# 	 |	  |	
#  moves = 1, 2, 3, 4, 5
# who_starts = 1
# every even move p1
