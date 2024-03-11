import pygame
import pygame.gfxdraw
import math
from sense_hat import SenseHat
sense = SenseHat()

# setup pygame
pygame.init()
screen = pygame.display.set_mode((300, 50))
pygame.display.set_caption('Temp Gauge')
running = True

# fill the screen with a solid color to clear it
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

# RENDER GAME HERE
temp = sense.get_temperature()
font = pygame.font.Font(None, 36)
text = font.render(str(temp), 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)

# Blit it all to the screen
screen.blit(background, (0, 0))
pygame.display.flip()


while running:
    # pol for events
    # a QUIT event means the user clicked the [x] button on the window

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    temp = round(sense.get_temperature(), 2)
    text = font.render(str(temp), 1, (10, 10, 10))
    background.fill((250, 250, 250))
    background.blit(text, textpos)
    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()