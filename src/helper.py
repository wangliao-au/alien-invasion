import pygame
import sys

from bullet import Bullet
from ufo import Ufo

class Helper:
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

    def create_fleet(self):
        """Create a fleet of ufos."""
        # Make an ufo and find the number of ufos in a row.
        # Spacing between each ufo is equal to half ufo width.
        new_ufo = Ufo(self)
        ufo_width, ufo_height = new_ufo.rect.size
        between_ufo =  1.69
        num_ufos = self.settings.screen_width // (ufo_width * between_ufo) + 1 # // returns an integer

        # Determine the number of rows of ufos that fit on the screen.
        ship_height = self.ship.rect.height
        space_y = (self.settings.screen_height - (4 * ufo_height) - ship_height)
        num_rows = space_y // (2 * ufo_height)

        # Create the full fleet of aliens.
        for row in range(num_rows):
            for i in range(int(num_ufos)):
                self.create_ufos(i, ufo_width, row, between_ufo)

    def create_ufos(self, i, width, row, between):
            new_ufo = Ufo(self)
            new_ufo.x = i * width * between
            new_ufo.rect.x = new_ufo.x
            new_ufo.rect.y = new_ufo.rect.height + 2 * new_ufo.rect.height * row
            self.ufos.add(new_ufo)

    def fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_stored:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        """Update the bullets"""
        self.bullets.update()

        # Delete the out-screen bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets)) To see the bullets being removed.

    def update_screen(self):
        """Update the screen"""
        # Redraw the screen with background color
        self.screen.fill(self.settings.bg_color)
        # Draw the ship, at the current location
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.ufos.draw(self.screen)

        # Update the surface
        pygame.display.flip()