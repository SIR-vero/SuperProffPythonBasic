import pygame, sys
import time

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15

BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
#LINE_COLOR = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC_TAC_TOE')
screen.fill(BG_COLOR)

board = [[0, 0, 0], 
		 [0, 0, 0], 
		 [0, 0, 0]]

def check_win():

	in_put = board
	player1_sym = 1
	player2_sym = 2

	if in_put[0][0] == player1_sym and in_put[0][1] == player1_sym and in_put[0][2] == player1_sym:
		return (1, 'h1')
	elif in_put[0][0] == player2_sym and in_put[0][1] == player2_sym and in_put[0][2] == player2_sym:
		return (2, 'h1')
		
	
	
	if in_put[1][0] == player1_sym and in_put[1][1] == player1_sym and in_put[1][2] == player1_sym:
		return (1, 'h2')
	elif in_put[1][0] == player2_sym and in_put[1][1] == player2_sym and in_put[1][2] == player2_sym:
		return (2, 'h2')
	
	if in_put[2][0] == player1_sym and in_put[2][1] == player1_sym and in_put[2][2] == player1_sym:
		return (1, 'h3')
	elif in_put[2][0] == player2_sym and in_put[2][1] == player2_sym and in_put[2][2] == player2_sym:
		return (2, 'h3')
	
	if in_put[0][0] == player1_sym and in_put[1][0] == player1_sym and in_put[2][0] == player1_sym:
		return (1, 'v1')
	elif in_put[0][0] == player2_sym and in_put[1][0] == player2_sym and in_put[2][0] == player2_sym:
		return (2, 'v1') 
	
	if in_put[0][1] == player1_sym and in_put[1][1] == player1_sym and in_put[2][1] == player1_sym:
		return (1, 'v2')
	elif in_put[0][1] == player2_sym and in_put[1][1] == player2_sym and in_put[2][1] == player2_sym:
		return (2, 'v2') 
	
	if in_put[0][2] == player1_sym and in_put[1][2] == player1_sym and in_put[2][2] == player1_sym:
		return (1, 'v3')
	elif in_put[0][2] == player2_sym and in_put[1][2] == player2_sym and in_put[2][2] == player2_sym:
		return (2, 'v3') 
	
	if in_put[0][0] == player1_sym and in_put[1][1] == player1_sym and in_put[2][2] == player1_sym:
		return (1, 'd1')
	elif in_put[0][0] == player2_sym and in_put[1][1] == player2_sym and in_put[2][2] == player2_sym:
		return (2, 'd1') 
	
	if in_put[0][2] == player1_sym and in_put[1][1] == player1_sym and in_put[2][0] == player1_sym:
		return (1, 'd2')
	elif in_put[0][2] == player2_sym and in_put[1][1] == player2_sym and in_put[2][0] == player2_sym:
		return (2, 'd2')
		
	return (0, 'nn')
	

def validate(row, col):
	return board[row][col] == 0

def game_input(row, col, moves):
	if moves % 2 == 1:
		if validate(row, col):
			board[row][col] = 1
			return True
		return False
	else :
		if validate(row, col):
			board[row][col] = 2
			return True
		return False

def draw_sym(row, col, moves):
	if moves % 2 == 1:
		pygame.draw.line(screen, (255, 255, 255), (col * 200 + 20, row * 200 + 20), (col * 200 + 180, row * 200 + 180), LINE_WIDTH)
		pygame.draw.line(screen, (255, 255, 255), (col * 200 + 180, row * 200 + 20), (col * 200 + 20, row * 200 + 180), LINE_WIDTH)
	else :
		pygame.draw.circle(screen, (255, 255, 255), (col * 200 + 100, row * 200 + 100), 70, LINE_WIDTH - 5)

def draw_win_line(x):
	if x == 'h1':
		pygame.draw.line(screen, (255, 255, 255), (10, 100), (590, 100), LINE_WIDTH+10)
	elif x == 'h2':
		pygame.draw.line(screen, (255, 255, 255), (10, 300), (590, 300), LINE_WIDTH+10)
	elif x == 'h3':
		pygame.draw.line(screen, (255, 255, 255), (10, 500), (590, 500), LINE_WIDTH+10)
	elif x == 'v1':
		pygame.draw.line(screen, (255, 255, 255), (100, 10), (100, 590), LINE_WIDTH+10)
	elif x == 'v2':
		pygame.draw.line(screen, (255, 255, 255), (300, 10), (300, 590), LINE_WIDTH+10)
	elif x == 'v3':
		pygame.draw.line(screen, (255, 255, 255), (500, 10), (500, 590), LINE_WIDTH+10)
	elif x == 'd1':
		pygame.draw.line(screen, (255, 255, 255), (10, 10), (590, 590), LINE_WIDTH+10)
	elif x == 'd2':
		pygame.draw.line(screen, (255, 255, 255), (590, 10), (10, 590), LINE_WIDTH+10)

def draw_lines():
	pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
	
	pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

	pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
	
	pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)
	
	
	
draw_lines()


font = pygame.font.Font('freesansbold.ttf', 30)
text = font.render("hemllo", False, (255,0,0))
screen.blit(text, (300,300))



moves = 1
# mainloop
running = True
while running:
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			print("Quit")
			running = False
			pygame.quit()
			sys.exit()
			quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			print("mouse in: x: ", event.pos[0], " y: ", event.pos[1])
			row = event.pos[1] // 200
			col = event.pos[0] // 200
			print("row : ", row, " col: ", col)
			if game_input(row, col, moves):
				draw_sym(row, col, moves)
				check = check_win()
				if check[0] == 1:
					print("player 1 won")
					draw_win_line(check[1])
					running = False
					#time.sleep(5)
				elif check[0] == 2:
					print("player 2 won")
					draw_win_line(check[1])
					running = False
					#time.sleep(5)
				elif moves == 9:
					print("draw!!!!")
					running = False
					#time.sleep(5)
					
				moves += 1
			
	pygame.display.update()
	
time.sleep(5)