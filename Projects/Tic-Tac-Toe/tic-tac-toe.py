import os
import time
import random
# a | b | c 
#---+---+---
# 	|	|	
#---+---+---
# 	|	|	

# in_put = [["a", "X", "O"],["d", "X", "O"],["g", "X", "O"]]

def draw_board(in_put, turn):	
	os.system('cls')
	
	print(" ",in_put[0][0]," | ",in_put[0][1]," | ",in_put[0][2],sep = "")
	print("---+---+---")
	print(" ",in_put[1][0]," | ",in_put[1][1]," | ",in_put[1][2],sep = "")
	print("---+---+---")
	print(" ",in_put[2][0]," | ",in_put[2][1]," | ",in_put[2][2],sep = "")
	
	print("\nSelect a Valid position to put a", turn)


def game_input(moves, who_starts, assigned_symbol):
	




player1 = input("Enter your name: ") # p1 = "Ayush"
player2 = input("Enter your Friend's name: ")

assigned_symbol = random.randint(0, 2) # 0, 1
if assigned_symbol == 0:
	print(player1, "is 'X'")
	print(player2, "is 'O'")
else :
	print(player1, "is 'O'")
	print(player2, "is 'X'")

who_starts = random.randint(0, 2) # 0, 1

if who_starts == 0:
	print(player1, "will start")
else :
	print(player2, "will start")
	

moves = 1
while moves <= 9:
	game_input(moves, who_starts, assigned_symbol)
	draw_board()
	check_win()
	




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
