class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ships settings
        # When the ship moves, 3 pixels / pass
        self.ship_speed = 3

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (200, 60, 60)
