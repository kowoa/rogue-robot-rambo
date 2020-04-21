# Game settings
SCREEN_TITLE = "ROGUE ROBOT RAMBO"
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
MAX_FPS = 60

# Fonts
FONT_NAME = "arial"

# Environmental properties
GRAVITY_ACC = 0.8  # Try to keep close to 1 else the player twitches up and down on platforms
WIND_VEL = 0  # Not used yet

# Platform arguments for testing
PLATFORM_LIST = [
    ((0, SCREEN_HEIGHT - 40), (SCREEN_WIDTH, 40)),
    ((SCREEN_WIDTH/2-50, SCREEN_HEIGHT*3/4), (100, 20)),
    ((125, SCREEN_HEIGHT-350), (100, 20)),
    ((350, 200), (100, 20)),
    ((175, 100), (50, 20))
]
