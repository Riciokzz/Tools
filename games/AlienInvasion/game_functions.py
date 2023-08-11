import sys

import pygame


def check_events():
    """Respond to key presses and mouse evens."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
