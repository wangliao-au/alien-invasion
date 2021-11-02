"""
Written by https://github.com/lia0wang on 01/11/2021
Powered and inspired by <Python Crash Course>
"""
import pygame

from src.helper import Helper

class AlienInvasion(Helper):
    """Overall class to manage game assets and behavior"""
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self.check_events()

            if self.stats.game_run:
                self.ship.update()
                self.update_bullets()
                self.update_ufos()
            
            self.update_screen()

if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()