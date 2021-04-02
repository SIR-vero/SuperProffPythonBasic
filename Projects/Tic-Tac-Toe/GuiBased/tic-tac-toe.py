import pygame, os

pygame.init()

img_surf = pygame.image.load(os.getcwd() + '\icon.png')
pygame.display.set_icon(img_surf)
pygame.display.set_caption('Tic-Tac-Toe')
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 0))

board = [[0,0,0],
		 [0,0,0],
		 [0,0,0]]


def draw_lines():
	pygame.draw.line(screen, (0,0,0), (200, 0), (200, 599), 10)
	pygame.draw.line(screen, (0,0,0), (400, 0), (400, 599), 10)
	pygame.draw.line(screen, (0,0,0), (0, 200), (599, 200), 10)
	pygame.draw.line(screen, (0,0,0), (0, 400), (599, 400), 10)

def validate(row, col):
	if board[row][col] == 0:
		True
	else:
		False

def draw_symbols():
	for i in range(3):
		for j in range(3):
			# Try to Complete
			

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
	pygame.draw.circle(screen, (0,0,0), (row*200 + 100, col*200 + 100), 80, 20)



draw_lines()

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
			if validate(row, col):
				game_input(row, col, moves)
				moves = moves + 1
	
	if running:
		pygame.display.update()		





# 415, 4
# 415//200, 4//200


#  0   1   2
#0   |   |  
# ---+---+---
#1   |   | 
# ---+---+---
#2   |   |    
	