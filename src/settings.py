# Game settings
SCREEN_TITLE = "ROGUE ROBOT RAMBO"
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
MAX_FPS = 60

# Fonts
FONT_NAME = "arial"

# Environmental properties
GRAVITY_ACC = 0.8  # Try to keep close to 1 else the player twitches up and down on platforms
WIND_VEL = 0  # Not used yet

# Platform arguments for testing
PLATFORM_LIST = [
    ((-20, SCREEN_HEIGHT - 40), (SCREEN_WIDTH + 40, 40)),
    ((SCREEN_WIDTH/2-30, SCREEN_HEIGHT*3/4), (1000, 20)),
    ((125, SCREEN_HEIGHT-350), (1000, 20)),
    ((350, 200), (1000, 20)),
    ((175, 100), (500, 20))
]
