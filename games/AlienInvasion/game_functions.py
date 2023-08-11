import sys

import pygame


def check_keydown_events(event, ship):
    """Respond to keypress."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Respond to key release."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """Respond to key presses and mouse evens."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event=event, ship=ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event=event, ship=ship)



def update_screen(ai_settings, screen, ship, game_character):
    """Update the screen during each loop"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    game_character.blitme()

    # Make the most recently event visible by refreshing.
    pygame.display.flip()
