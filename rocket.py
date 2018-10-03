import pygame


class Rocket:
    """A class to describe rocket and it's mechanics"""
    def __init__(self, screen):
        """Initial rocket settings."""
        self.screen = screen

        # Load rocket image and use PyGame Rect function to manipulate rectangular areas.
        self.rocket_image = pygame.image.load('rocket.png')
        self.rocket_rect = self.rocket_image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Starting position of the rocket.
        self.rocket_rect.centerx = self.screen_rect.centerx
        self.rocket_rect.bottom = self.screen_rect.bottom

        # Smooth movement flags
        self.moving_right = False
        self.moving_left = False

    def new_position(self):
        """Rocket position update which depends on the smooth movement flags."""
        # Move rocket to the right and limit it to the right side.
        if self.moving_right and self.rocket_rect.right < self.screen_rect.right:
            self.rocket_rect.centerx += 1
        # Move rocket to the left and limit it to the left side.
        if self.moving_left and self.rocket_rect.left > 0:
            self.rocket_rect.centerx -= 1

    def image_draw(self):
        """Draw the rocket on the screen at defined position."""
        self.screen.blit(self.rocket_image, self.rocket_rect)
