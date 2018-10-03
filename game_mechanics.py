import sys
import pygame
from missile import Missile
from alien import Alien


def event_type(game_para, rocket, screen, missiles):
    """Function to respond key presses."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Turn off game window.
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Make Rocket smooth movement right side flag True.
                rocket.moving_right = True
            if event.key == pygame.K_LEFT:
                # Make Rocket smooth movement left side flag True.
                rocket.moving_left = True
            elif event.key == pygame.K_SPACE:
                # Create a new missile and store it to missiles Group() with a limitation condition.
                if len(missiles) < game_para.missile_amount:
                    new_missile = Missile(game_para, screen, rocket)
                    missiles.add(new_missile)
            elif event.key == pygame.K_q:
                # Turn off game window with keyboard 'q' button.
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # Make Rocket smooth movement right side flag False.
                rocket.moving_right = False
            if event.key == pygame.K_LEFT:
                # Make Rocket smooth movement left side flag False.
                rocket.moving_left = False


def screen_renew(screen, rocket, game_para, missiles, aliens):
    """Function to update/renew screen and images on it."""
    # Fill screen with set color.
    screen.fill(game_para.display_color)
    # Place missiles on the screen but behind all elements.
    for missile in missiles.sprites():
        missile.missile_draw()
    # Place rocket on the screen.
    rocket.image_draw()
    # Place alien elements on the screen.
    # draw() function draws each element in the group at the position defined by its Rect attribute"""
    aliens.draw(screen)
    # Update the full display to the screen.
    pygame.display.flip()


def missile_management(missiles, aliens):
    """A function to describe missiles placement and removal."""
    # Instance for missiles position updates.
    missiles.update()

    # Check if missile hit the alien.
    pygame.sprite.groupcollide(missiles, aliens, True, True)

    # Remove missiles from the Group() that reached screen top.
    for missile in missiles.copy():
        if missile.rect.bottom <= 0:
            missiles.remove(missile)


def aliens_in_row(game_para, alien_width):
    """A function to get an alien number which can be placed in a single row."""
    alien_place_x = game_para.screen_width - (2 * alien_width)
    alien_in_row_x = int(alien_place_x / (2 * alien_width))
    return alien_in_row_x


def aliens_rows(game_para, alien_height, rocket_height):
    """A function to get an alien row number which can be placed in available space."""
    alien_place_y = (game_para.screen_height - (3 * alien_height) -
                     rocket_height)
    row_number_y = int(alien_place_y / (2 * alien_height))
    return row_number_y


def new_aliens(game_para, screen, aliens, alien_each, row_number_y):
    """A function to create an alien and describe a full row of aliens.."""
    # Create an alien.
    alien = Alien(game_para, screen)
    # Define a space between each alien.. Defining number of aliens in a row.
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_each)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number_y)
    aliens.add(alien)


def alien_army(game_para, screen, aliens, rocket):
    """A function to describe a row full of aliens."""
    # Create an alien.
    alien = Alien(game_para, screen)
    alien_in_row_x = aliens_in_row(game_para, alien.rect.width)
    aliens_rows_in_y = aliens_rows(game_para, alien.rect.height,
                                   rocket.rocket_rect.height)

    # Whole aliens army.
    for row in range(aliens_rows_in_y):
        for alien_each in range(alien_in_row_x):
            new_aliens(game_para, screen, aliens, alien_each, row)


def alien_army_side(game_para, aliens):
    """A function to react when whole alien army reaches left or right side of the scree,"""
    for alien in aliens.sprites():
        if alien.side_reach():
            change_alien_army_direction(game_para, aliens)
            break


def change_alien_army_direction(game_para, aliens):
    """A function to describe whole army drop down and change it's direction."""
    for alien in aliens.sprites():
        alien.rect.y += game_para.alien_army_drop_speed
    game_para.alien_move_direction *= -1


def alien_new_position(game_para, aliens):
    """
    A function to check if alien army reached left or right side of the screen.
    After it update the whole alien army position.
    """
    alien_army_side(game_para, aliens)
    aliens.update()
