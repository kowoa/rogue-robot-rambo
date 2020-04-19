# Game settings
SCREEN_TITLE = "ROGUE ROBOT RAMBO"
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
MAX_FPS = 60

# Fonts
FONT_NAME = "arial"

# Player properties
PLAYER_ACC = 0.5
# FUTURE: different frictions for different platforms
PLAYER_FRICTION = -0.12  # Make sure this is negative
PLAYER_JUMP_VEL = -18  # Make sure this is negative
PLAYER_JUMP_DELAY = 500

# Environmental properties
GRAVITY_ACC = 0.8  # Try to keep close to an integer else the player twitches up and down on platforms

# Platform arguments for testing
PLATFORM_LIST = [
    ((0, SCREEN_HEIGHT - 40), (SCREEN_WIDTH, 40)),
    ((SCREEN_WIDTH/2-50, SCREEN_HEIGHT*3/4), (100, 20)),
    ((125, SCREEN_HEIGHT-350), (100, 20)),
    ((350, 200), (100, 20)),
    ((175, 100), (50, 20))
]