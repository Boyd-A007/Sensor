import pygame
import pygame.gfxdraw
import math
from sense_hat import SenseHat
sense = SenseHat()

# setup pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    # pol for events
    # a QUIT event means the user clicked the [x] button on the window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a solid color to clear it
    screen.fill("grey")

    # RENDER GAME HERE
    temp = sense.get_temperature()
    print(temp)

    screen.blit(temp)

    # flip the display to put the work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()