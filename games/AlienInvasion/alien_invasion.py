import os
import sys

import pygame


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Start main loop for game.
    while True:

        # Check for keyboard and mouse movements and clicks.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recentrly drawn screen visible.
        pygame.display.flip()

run_game()
