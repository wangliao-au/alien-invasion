import pygame
import sys

from time import sleep

from pygame import mouse

from src.helpers.setting import Settings
from src.helpers.game_stats import GameStats
from src.helpers.button import Button

from src.objects.ship import Ship
from src.objects.bullet import Bullet
from src.objects.ufo import Ufo

class AlienInvasion:
    def __init__(self):
        """Initialize the game and create fame resources"""
        pygame.init()
        self.settings = Settings()

        # Set the screen dimensions and caption for display
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.icon = pygame.image.load('images/alien.png')
        pygame.display.set_caption("LGames - Alien Invasion")
        pygame.display.set_icon(self.icon)

        # Create an instance to store game stats.
        self.stats = GameStats(self)

        # Pass self to Instances so they can access the attributes in AI
        # Create ship, bullets and ufos
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.ufos = pygame.sprite.Group()

        self.create_fleet()

        # Make the play button.
        self.play_button = Button(self, "Play")

    def check_events(self):
            """Respond to keypresses and mouse events."""
            for event in pygame.event.get():
                self.check_quit_event(event)
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    self.check_play_button(mouse_pos)
                elif event.type == pygame.KEYDOWN:
                    self.check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self.check_keyup_events(event)

    def check_quit_event(self, event):
        """Response to quit command"""
        if event.type == pygame.QUIT:
                sys.exit()

    def check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_run:
            self.settings.initialize_dynamic_settings()
            self.start_the_game()
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def check_keydown_events(self, event):
        """Response to key press"""
        # Use elif since we only check the condition of one key each time
        if event.key == pygame.K_p and not self.stats.game_run:
            self.settings.initialize_dynamic_settings()
            self.start_the_game()
        elif event.key == pygame.K_RIGHT:
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

    def update_ufos(self):
        """Update the positions of all ufos in the fleet."""
        self.check_fleet_edges()
        self.ufos.update()

        # Look for ufo-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.ufos):
            self.ship_hit()

        # Check if the ufos reached the bottom:
        self.check_ufos_bottom()

    def update_bullets(self):
        """Update the bullets"""
        self.bullets.update()

        # Delete the out-screen bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self.check_bullet_ufo_collisions()

    def update_screen(self):
        """Update the screen"""
        # Redraw the screen with background color
        self.screen.fill(self.settings.bg_color)
        # Draw the ship, at the current location
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.ufos.draw(self.screen)

        # If the game is inactive, draw the play button.
        if not self.stats.game_run:
            self.play_button.draw_button()

        # Update the surface
        pygame.display.flip()

    def create_ufos(self, i, row):
            # Create an alien and place it in the row.
            ufo = Ufo(self)
            ufo_width, ufo_height = ufo.rect.size
            ufo.horizon = ufo_width + 2 * ufo_width * i
            ufo.rect.x = ufo.horizon
            ufo.rect.y = ufo_height + 2 * ufo_height * row
            self.ufos.add(ufo)

    def create_fleet(self):
        """Create a fleet of ufos."""
        # Make an ufo and find the number of ufos in a row.
        # Spacing between each ufo is equal to half ufo width.
        new_ufo = Ufo(self)
        ufo_width, ufo_height = new_ufo.rect.size
        available_space_x = self.settings.screen_width - (2 * ufo_width)
        num_ufos = available_space_x // (2 * ufo_width) # // returns an integer

        # Determine the number of rows of ufos that fit on the screen.
        ship_height = self.ship.rect.height
        space_y = (self.settings.screen_height - (3 * ufo_height) - ship_height)
        num_rows = space_y // (2 * ufo_height)

        # Create the full fleet of aliens.
        for row in range(num_rows):
            for i in range(num_ufos):
                self.create_ufos(i, row)

    def check_fleet_edges(self):
        """Respond if any ufos have reached an edge."""
        for ufo in self.ufos.sprites():
            if ufo.is_hit_edges():
                self.change_fleet_direction()
                break
    
    def change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for ufo in self.ufos.sprites():
            ufo.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_stored:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def check_bullet_ufo_collisions(self):
        """Respond to collisions."""
        # Check if the bullet hit an ufo, get rid of the ufo if so.
        pygame.sprite.groupcollide(self.bullets, self.ufos, True, True)

        # If ufos are all destroyed
        if not self.ufos:
            # Get rid of eisiting bullets and create new fleet.
            self.bullets.empty()
            self.create_fleet()

            self.settings.ufo_level_up()            
            self.settings.ship_level_up()
            
    def ship_hit(self):
        """Respond to the ship being hit by an ufo."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            # Get rid of any remaining ufos and bullets.
            self.ufos.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self.create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(2)
        else:
            self.stats.game_run = False
            pygame.mouse.set_visible(True)

    def check_ufos_bottom(self):
        """Check if any ufos have reached the bottom of screen."""
        screen_rect = self.screen.get_rect()
        for ufo in self.ufos.sprites():
            if ufo.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    def start_the_game(self):
        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_run = True
        self.ufos.empty()
        self.bullets.empty()
        
        # Create a new fleet snd center the ship.
        self.create_fleet()
        self.ship.center_ship()