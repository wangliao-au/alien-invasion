"""
Written by https://github.com/lia0wang on 01/11/2021
Powered and inspired by <Python Crash Course>
"""
import pygame

from setting import Settings
from ship import Ship
from helper import Helper

class AlienInvasion(Helper):
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game and create fame resources"""
        pygame.init()
        self.settings = Settings()

        # Set the screen dimensions and caption for display
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.icon = pygame.image.load('images/alien.png')
        pygame.display.set_caption("LGames - Alien Invasion")
        pygame.display.set_icon(self.icon)

        # Pass the alienInvasion instance(self) to Ship, 
        # so Ship can access the game's resource
        # assign the Ship instance to self.ship
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.ufos = pygame.sprite.Group()

        self.create_fleet()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self.check_events()
            self.ship.update()
            self.update_bullets()
            self.update_screen()

if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()