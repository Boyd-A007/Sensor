import pygame

# setup pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector(screen.get_width() / 2, screen.get_height() /2)

while running:
    # pol for events
    # a QUIT event means the user clicked the [x] button on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a solid color to clear it
    screen.fill("purple")

    # RENDER GAME HERE
    pygame.draw.circle(screen, "red", player_pos, 40)

    # flip the display to put the work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()