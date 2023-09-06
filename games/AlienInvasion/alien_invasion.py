import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings=ai_settings, screen=screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens)

    # Start main loop for game.
    while True:

        # Check for user inputs.
        gf.check_events(ai_settings=ai_settings,
                        screen=screen,
                        stats=stats,
                        play_button=play_button,
                        ship=ship,
                        aliens=aliens,
                        bullets=bullets)

        if stats.game_active:
            # Update position of ship.
            ship.update()

            # Update any bullets on screen.
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

            # Update aliens on screen.
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

            # Update screen base by previous updates.
            gf.update_screen(ai_settings=ai_settings,
                             screen=screen,
                             stats=stats,
                             ship=ship,
                             aliens=aliens,
                             bullets=bullets,
                             play_button=play_button)


run_game()
