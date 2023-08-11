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

        # Check for user inputs.
        gf.check_events(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)

        # Update position of ship.
        ship.update()

        # Update any bullets on screen.
        gf.update_bullets(bullets)

        # Update screen base by previous updates.
        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)


run_game()
