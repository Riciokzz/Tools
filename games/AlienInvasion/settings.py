class Settings:
    """A class to store all settings for Alien Invasion game."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (173, 196, 206)

        # Ship speed
        self.ship_speed_factor = 1.5
