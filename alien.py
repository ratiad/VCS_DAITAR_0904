import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to specify an alien."""
    def __init__(self, game_para, screen):
        """Initial slien settings."""
        super().__init__()
        self.screen = screen
        self.game_para = game_para

        # Load alien image and use PyGame Rect function to manipulate rectangular areas.
        self.image = pygame.image.load('alien_ship.png')
        self.rect = self.image.get_rect()

        # Starting position of the alien ship.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Making alien's start point. Storing as a decimal value.
        self.x = float(self.rect.x)

    def image_draw(self):
        """Draw an alien on the screen at defined position."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """A function to describe alien movement."""
        self.x += (self.game_para.alien_speed * self.game_para.alien_move_direction)
        self.rect.x = self.x

    def side_reach(self):
        """A function to check if whole alien army reached left or right side."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
