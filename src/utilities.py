SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720


def convert_to_pygame(pos):
    """
    Converts positional coordinates from pymunk to pygame
    :param pos: tuple containing x, y pymunk coordinates
    :return: tuple containing x, y pygame coordinates
    """
    # For some reason using this method will convert all coordinates to
    # standard mathematical rectangular coordinates
    return pos[0], -pos[1] + SCREEN_HEIGHT

