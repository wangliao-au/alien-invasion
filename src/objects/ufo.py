import pygame
from pygame.sprite import Sprite

class Ufo(Sprite):
    """A class to represent a single ufo in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien image asnd set its rect attribute.
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.horizon = float(self.rect.x)
    
    def update(self):
        """Move the ufo to the right."""
        # direction = -1/1, multiply by speed to move either left or right.
        self.horizon += (self.settings.ufo_speed * self.settings.fleet_direction)
        self.rect.x = self.horizon

    def is_hit_edges(self):
        """Return True if ufo is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right - self.rect.width - 10 or self.rect.left <= 0:
            return True