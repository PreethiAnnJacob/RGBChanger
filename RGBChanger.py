'''Implements a screen with varying RGB colours
Key r- Red colour
Key g- Green colour
Key b- Blue colour
Esc- Exit game
'''

import sys # for interpreter related interactions
import pygame
from pygame.locals import FULLSCREEN, KEYDOWN, K_ESCAPE, K_r, K_b, K_g

screen=pygame.display.set_mode((0,0), FULLSCREEN)
clock=pygame.time.Clock()
colour="blue"
i=0
inc=True

while True:
	while i>=0 and i<=255:
		clock.tick(1000)
		if colour=="red": 
			screen.fill((i,0,0))
		elif colour=="green":
			screen.fill((0,i,0))
		elif colour=="blue":
			screen.fill((0,0,i))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type==KEYDOWN:
				if event.key==K_ESCAPE:
					print("Thanks for playing!")
					sys.exit(0)
				if event.key==K_r:
					colour="red"
					continue
				if event.key==K_g:
					colour="green"
					continue
				if event.key==K_b:
					colour="blue"
					continue
		if i==0:
			inc=True
		elif i==255:
			inc=False
		if inc:
			i+=1
		else:
			i-=1

