import sys

import pygame

from settings import Settings


def run_game():
    # Initialize game, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.screen_width, ai_settings.screen_height)
    pygame.display.set_caption("Alien Invasion")

    # Set up background color.
    bg_color = (ai_settings.bg_color)

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
