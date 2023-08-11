import pygame

from settings import Settings
from ship import Ship, game_character as gc
import game_functions as gf


def run_game():
    # Initialize game, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(screen)
    character = gc(screen)

    # Start main loop for game.
    while True:

        # Check for keyboard and mouse movements and clicks.
        gf.check_events()

        # Redraw the screen during each pass through the loop.
        # Redraw the most recently screen while clearing old visible screen.
        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship, game_character=character)


run_game()
