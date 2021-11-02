import pygame
from pygame.sprite import Sprite

class Ufo(Sprite):
    """A class to represent a single ufo in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image asnd set its rect attribute.
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = 0
        self.rect.y = 0

        # Store the alien's exact horizontal position
        self.horizon = float(self.rect.x)