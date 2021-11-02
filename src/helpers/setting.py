class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        self.ship_limit = 3

        self.bullet_width = 6
        self.bullet_stored = 10
        self.bullet_height = 15
        self.bullet_color = (200, 60, 60)
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        # Ships settings
        self.ship_speed = 6
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 6
        self.bullet_stored = 3
        
        # Ufo settings
        self.ufo_speed = 2
        self.fleet_drop_speed = 5

        # Scoring
        self.ufo_points = 750

    def ship_level_up(self):
        """Ship becomes stronger."""

        # Ships improved settings
        self.ship_increase_hp = 0.5
        self.ship_increase_speed = 1

        self.ship_limit += self.ship_increase_hp
        self.ship_speed += self.ship_increase_speed

        # Bullet improved settings
        self.bullet_increase_width = 1.75
        self.bullet_increase_store = 1
        self.bullet_increase_speed = 1

        self.bullet_width *= self.bullet_increase_width
        self.bullet_stored += self.bullet_increase_store
        self.bullet_speed += self.bullet_increase_speed

    def ufo_level_up(self):
        """Ufos become stronger."""
        self.ufo_increase_speed = 1
        self.fleet_increase_drop_speed = 5
        self.ufo_increase_points = 1.5

        self.fleet_drop_speed += self.fleet_increase_drop_speed
        self.ufo_speed += self.ufo_increase_speed
        self.ufo_points *= self.ufo_increase_points