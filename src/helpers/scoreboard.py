from time import sleep
import pygame.font

from pygame.sprite import Group
from src.objects.ship import Ship

class Scoredboard:
    """A class to report scoring information."""
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_colour = (255, 255, 255)
        self.text_colour_high = (255, 0, 0)
        self.text_colour_level = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48, False, True)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the socre into a rendered image."""
        # int -> str -> image
        rounded_score = round(int(self.stats.score), -1)
        score_str = "Current: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_colour, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = 0
        self.score_rect.top = 10

    def prep_high_score(self):
        """Turn the highest scofre into a rendered image."""
        high_score = round(int(self.stats.high_score), -1)
        high_score_str = "Best: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_colour_high, self.settings.bg_color)

        # Center the high score horizontally at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = "LV." + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_colour_level, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 10
        self.level_rect.top = self.score_rect.top

    def prep_ships(self):
        """Show how many ships are left."""
        # Create an empty group
        self.ships = Group()
        for i in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = self.screen_rect.width - ship.rect.width
            ship.rect.y = 2 * (self.score_rect.height + self.level_rect.height) + i * ship.rect.height
            # Fill the group with new ships.
            self.ships.add(ship)

    def show_score(self):
        """Draw score, level, ships group to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Check to see if there is a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()