import pygame, os

pygame.init()

WIDTH = 1000
HEIGHT = 600

img_surf = pygame.image.load(os.getcwd() + '\icon.png')
pygame.display.set_icon(img_surf)
pygame.display.set_caption('Tic-Tac-Toe')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 0))

board = [[0,0,0],
		 [0,0,0],
		 [0,0,0]]

def check_win(in_put):
	
	player1_sym = 1
	player2_sym = 2

	if in_put[0][0] == player1_sym and in_put[0][1] == player1_sym and in_put[0][2] == player1_sym:
		return ["h1", 1]
	elif in_put[0][0] == player2_sym and in_put[0][1] == player2_sym and in_put[0][2] == player2_sym:
		return ["h1", 2]

	if in_put[1][0] == player1_sym and in_put[1][1] == player1_sym and in_put[1][2] == player1_sym:
		return ["h2", 1]
	elif in_put[1][0] == player2_sym and in_put[1][1] == player2_sym and in_put[1][2] == player2_sym:
		return ["h2", 2]
	
	if in_put[2][0] == player1_sym and in_put[2][1] == player1_sym and in_put[2][2] == player1_sym:
		return ["h3", 1]
	elif in_put[2][0] == player2_sym and in_put[2][1] == player2_sym and in_put[2][2] == player2_sym:
		return ["h3", 2] 
	
	if in_put[0][0] == player1_sym and in_put[1][0] == player1_sym and in_put[2][0] == player1_sym:
		return ["v1", 1]
	elif in_put[0][0] == player2_sym and in_put[1][0] == player2_sym and in_put[2][0] == player2_sym:
		return ["v1", 2] 
	
	if in_put[0][1] == player1_sym and in_put[1][1] == player1_sym and in_put[2][1] == player1_sym:
		return ["v2", 1]
	elif in_put[0][1] == player2_sym and in_put[1][1] == player2_sym and in_put[2][1] == player2_sym:
		return ["v2", 2] 
	
	if in_put[0][2] == player1_sym and in_put[1][2] == player1_sym and in_put[2][2] == player1_sym:
		return ["v3", 1]
	elif in_put[0][2] == player2_sym and in_put[1][2] == player2_sym and in_put[2][2] == player2_sym:
		return ["v3", 2]
	
	if in_put[0][0] == player1_sym and in_put[1][1] == player1_sym and in_put[2][2] == player1_sym:
		return ["d1", 1]
	elif in_put[0][0] == player2_sym and in_put[1][1] == player2_sym and in_put[2][2] == player2_sym:
		return ["d1", 2]
	
	if in_put[0][2] == player1_sym and in_put[1][1] == player1_sym and in_put[2][0] == player1_sym:
		return ["d2", 1]
	elif in_put[0][2] == player2_sym and in_put[1][1] == player2_sym and in_put[2][0] == player2_sym:
		return ["d2", 2]
		
	return ["xx", 0]

def draw_win_line(line):
	if line == "h1":
		pygame.draw.line(screen, (0,0,0), (0, 100), (599, 100), 30)
	elif line == "h2":
		pygame.draw.line(screen, (0,0,0), (0, 300), (599, 300), 30)
	elif line == "h3":
		pygame.draw.line(screen, (0,0,0), (0, 500), (599, 500), 30)
	elif line == "v1":
		pygame.draw.line(screen, (0,0,0), (100, 0), (100, 599), 30)
	elif line == "v2":
		pygame.draw.line(screen, (0,0,0), (300, 0), (300, 599), 30)
	elif line == "v3":
		pygame.draw.line(screen, (0,0,0), (500, 0), (500, 599), 30)
	elif line == "d1":
		pygame.draw.line(screen, (0,0,0), (0, 0), (599, 599), 30)
	elif line == "d2":
		pygame.draw.line(screen, (0,0,0), (599, 0), (0, 599), 30)
	
def draw_lines():
	pygame.draw.line(screen, (0,0,0), (200, 0), (200, 599), 10)
	pygame.draw.line(screen, (0,0,0), (400, 0), (400, 599), 10)
	pygame.draw.line(screen, (0,0,0), (0, 200), (599, 200), 10)
	pygame.draw.line(screen, (0,0,0), (0, 400), (599, 400), 10)

def validate(row, col):
	if board[row][col] == 0:
		return True
	else:
		return False

def draw_symbols():
	for i in range(3):
		for j in range(3):
			if board[i][j] == 1:
				draw_cross(i, j)
			elif board[i][j] == 2:
				draw_circle(i, j)

def game_input(row, col, moves):
	if moves%2 == 1:
		board[row][col] = 1
	else:
		board[row][col] = 2
	
	draw_symbols()

def draw_cross(row, col):
	pygame.draw.line(screen, (0,0,0), (col*200 + 10, row*200 + 10), (col * 200 + 190, row*200 + 190), 20)
	pygame.draw.line(screen, (0,0,0), (col*200 + 190,row*200 + 10), (col * 200 + 10, row*200 + 190), 20)

def draw_circle(row, col):
	pygame.draw.circle(screen, (0,0,0), (col*200 + 100, row*200 + 100), 80, 20)

def draw_scoreboard():
	pygame.draw.rect(screen, (0, 255, 255), (601, 0, 400, 600))
	font = pygame.font.Font("ComicSansMS3.ttf", 30)
	text = font.render("player1 : X", True, (0,0,0))
	screen.blit(text, (800, 100))
	text = font.render("player2 : O", True, (0,0,0))
	screen.blit(text, (800, 150))

def draw_reset_button():
	pygame.draw.rect(screen, (211, 211, 211), (611, 10, 150, 50))
	font = pygame.font.Font("ComicSansMS3.ttf", 30)
	text = font.render("RESET", True, (0,0,0))
	screen.blit(text, (631, 15))

draw_lines()
draw_scoreboard()
draw_reset_button()

play = True
running = True
moves = 1
while running:
	for event in pygame.event.get(): 
		#print(event)
		if event.type == pygame.QUIT:
			print(event.type)
			pygame.quit()
			running = False
			break
		if event.type == pygame.MOUSEBUTTONDOWN:
			x = event.pos[0]
			y = event.pos[1]
			#print(x, y)
			row = y//200
			col = x//200
			if validate(row, col) and play:
				game_input(row, col, moves)
				check = check_win(board)
				if check[1] == 1:
					print("player 1 WON!!!")
					font = pygame.font.Font("ComicSansMS3.ttf", 30)
					text = font.render("player1 WON!!!", True, (0,0,0))
					screen.blit(text, (700, 270))
					draw_win_line(check[0])
					play = False
				elif check[1] == 2:
					print("player 2 WON!!!")
					font = pygame.font.Font("ComicSansMS3.ttf", 30)
					text = font.render("player2 WON!!!", True, (0,0,0))
					screen.blit(text, (700, 270))
					draw_win_line(check[0])
					play = False
				elif moves == 9:
					print("DRAW!!!")
					font = pygame.font.Font("ComicSansMS3.ttf", 30)
					text = font.render("DRAW", True, (0,0,0))
					screen.blit(text, (700, 270))
					play = False
				moves = moves + 1
	
	if running:
		pygame.display.update()		



# 415, 4
# 415//200, 4//200


#  0   1   2
#0   |   |  	(h1, 1)
# ---+---+---
#1   |   | 		(h2, 1)
# ---+---+---
#2   |   |    	h3

#  	v1 v2 v3
	