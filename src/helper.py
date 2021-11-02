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
        # Make an ufo.
        new_ufo = Ufo(self)
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