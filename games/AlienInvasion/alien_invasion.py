import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    # Make a ship.
    ship = Ship(screen)

    # Start main loop for game.
    while True:

        # Check for keyboard and mouse movements and clicks.
        gf.check_events()

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Redraw the most recently screen while clearing old visible screen.
        pygame.display.flip()


run_game()
