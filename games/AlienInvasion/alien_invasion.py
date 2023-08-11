import pygame
from pygame.sprite import Group

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
    ship = Ship(ai_settings=ai_settings, screen=screen)
    bullets = Group()

    # Start main loop for game.
    while True:

        # Check for keyboard and mouse movements and clicks.
        gf.check_events(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)
        ship.update()

        # Redraw the screen during each pass through the loop.
        # Redraw the most recently screen while clearing old visible screen.
        bullets.update()
        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)


run_game()
