import sys

import pygame


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Set up background color.
    bg_color = (230, 230, 230)

    # Start main loop for game.
    while True:

        # Check for keyboard and mouse movements and clicks.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)

        # Redraw the most recently screen while clearing old visible screen.
        pygame.display.flip()


run_game()
