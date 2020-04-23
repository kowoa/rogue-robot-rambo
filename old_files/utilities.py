SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720


def convert_coordinates(pos):
    """
    Converts positional coordinates from pymunk to pygame or vice versa
    :param pos: tuple containing x, y pymunk or pygame coordinates
    :return: tuple containing x, y pygame or pymunk coordinates, respectively
    """
    return pos[0], -pos[1] + SCREEN_HEIGHT
