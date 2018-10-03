import pygame
from parameters import Parameters
from rocket import Rocket
import game_mechanics as gm
from pygame.sprite import Group


def game_function():
    """Main function to initialize Space Invaders game."""
    pygame.init()
    game_para = Parameters()

    # Game screen properties.
    screen = pygame.display.set_mode((game_para.screen_width,
                                      game_para.screen_height))
    pygame.display.set_caption('Space Invaders')

    # Make a rocket.
    rocket = Rocket(screen)

    # Make a group of an aliens.
    aliens = Group()

    # Make a group where all fired missiles will be stored.
    missiles = Group()

    # Create a row of an aliens.
    gm.alien_army(game_para, screen, aliens, rocket)

    # Main loop of the Space Invaders game.
    while True:
        # Call for game event function.
        gm.event_type(game_para, rocket, screen, missiles)
        # Instance for Rocket smooth movement.
        rocket.new_position()
        # Call for missiles add and remove function.
        gm.missile_management(missiles, aliens)
        # Call for alien update function.
        gm.alien_new_position(game_para, aliens)
        # Call for the screen renew function.
        gm.screen_renew(screen, rocket, game_para, missiles, aliens)


game_function()
