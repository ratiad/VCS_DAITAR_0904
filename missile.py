import pygame
from pygame.sprite import Sprite


class Missile(Sprite):
    """A class to describe missile mechanics."""
    def __init__(self, game_para, screen, rocket):
        """Initial missile settings."""
        super().__init__()
        self.screen = screen

        # Missile rect creation at coordinates (0,0)
        self.rect = pygame.Rect(0, 0, game_para.missile_width,
                                game_para.missile_height)
        # Set missile at the front of the rocket.
        self.rect.centerx = rocket.rocket_rect.centerx
        self.rect.top = rocket.rocket_rect.top

        # Making missile's start point. Storing as a decimal value.
        self.y = float(self.rect.y)

        # Defining color of the missile and it's speed.
        self.missile_color = game_para.missile_color
        self.missile_speed = game_para.missile_speed

    def update(self):
        """A function to describe missile travel path along y axis."""
        # Updating missile decimal position after firing it.
        self.y -= self.missile_speed
        # Updating missile rect position after firing it.
        self.rect.y = self.y

    def missile_draw(self):
        """A function to draw a missile to the screen."""
        pygame.draw.rect(self.screen, self.missile_color, self.rect)
