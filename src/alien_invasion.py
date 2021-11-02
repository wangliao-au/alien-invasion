"""
Written by https://github.com/lia0wang on 01/11/2021
Powered and inspired by <Python Crash Course>
"""
import sys

from setting import Settings
from ship import Ship
from bullet import Bullet

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
        self.icon = pygame.image.load('images/alien.png')

        pygame.display.set_caption("LGames - Alien Invasion")
        pygame.display.set_icon(self.icon)

        # Pass the alienInvasion instance(self) to Ship, 
        # so Ship can access the game's resource
        # assign the Ship instance to self.ship
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self.check_events()
            self.ship.update()
            self.bullets.update()
            self.update_screen()

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            self.check_quit_event(event)
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_quit_event(self, event):
        """Response to quit command"""
        if event.type == pygame.QUIT:
                sys.exit()

    def check_keydown_events(self, event):
        """Response to key press"""
        # Use elif since we only check the condition of one key each time
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def check_keyup_events(self, event):
        """Response to key up"""
        # Use elif since we only check the condition of one key each time
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def update_screen(self):
        """Update the screen"""
        # Redraw the screen with background color
        self.screen.fill(self.settings.bg_color)
        # Draw the ship, at the current location
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Update the surface
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()