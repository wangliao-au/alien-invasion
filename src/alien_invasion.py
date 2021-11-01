"""
Written by https://github.com/lia0wang on 01/11/2021
Powered and inspired by <Python Crash Course>
"""
import sys

from setting import Settings
from ship import Ship

import pygame
from pygame.constants import NOFRAME

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game and create fame resources"""
        pygame.init()
        self.settings = Settings()

        # Set the screen dimensions and caption for display
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("LGames - Alien Invasion")

        # Pass the alienInvasion instance(self) to Ship, 
        # so Ship can access the game's resource
        # assign the Ship instance to self.ship
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        """Update the screen"""
        # Redraw the screen with background color
        self.screen.fill(self.settings.bg_color)
        # Draw the ship, at the current location
        self.ship.blitme()

        # Update the surface
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()