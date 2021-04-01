import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill((255, 0, 0))

running = True
while running:
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			pygame.quit()
			running = False
			break
	if running:
		pygame.display.update()