import sys

import pygame


def check_events(ship):
    """Respond to key presses and mouse evens."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship, game_character):
    """Update the screen during each loop"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    game_character.blitme()

    # Make the most recently event visible by refreshing.
    pygame.display.flip()
