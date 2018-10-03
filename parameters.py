class Parameters:
    """A class to place all required basic parameters of the game"""
    def __init__(self):
        """Initial game settings."""
        # Screen parameters (color and dimensions).
        self.display_color = (0, 0, 80)
        self.screen_width = 1200
        self.screen_height = 800

        # Missile parameters.
        self.missile_speed = 1
        self.missile_width = 3
        self.missile_height = 10
        self.missile_color = 255, 255, 255
        self.missile_amount = 3

        # Alien parameters.
        self.alien_speed = 1
        self.alien_army_drop_speed = 10
        # Moving to the right of entire alien army number '1' represents right.
        # Moving to the right of entire alien army number '-1' represents left.
        self.alien_move_direction = 1
