from random import choice
from string import ascii_lowercase
import time
import asyncio
import pygame
pygame.init()

letter = choice(ascii_lowercase)
score = 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
print(letter)
pygameLetter = "K_0"

# pygame things :)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('TypeTest')
font = pygame.font.Font('FreeSansBold.ttf', 32)
text = font.render(letter, True, black)
textRect = text.get_rect()
textRect.center = (500 // 2, 500 // 2)


while True:
 	
	screen.fill(white)
	screen.blit(text, textRect)
 
	for event in pygame.event.get():
 
		if event.type == pygame.QUIT:
 
			pygame.quit()
 
			quit()

		if event.type == pygame.KEYDOWN:
			if pygame.key.name(event.key) == letter :
				print('huzzah')
				# probably an inefeciant (spelled wrong but that's fine)way to do this, but it works so 🤷
				letter = choice(ascii_lowercase)
				text = font.render(letter, True, black)
				textRect = text.get_rect()
				textRect.center = (500 // 2, 500 // 2)
				
		pygame.display.update()

