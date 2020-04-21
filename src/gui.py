class Button():
    def __init__(self, x, y, width, height, color, text = 'None'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text

    # Use this method to display a button on the position of the scren for your liking
    # Enter a rgb color for outline parameter
    def create(self, screen, text_size, text_color, outline = None):
        if outline == None:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != 'None':
            pygame.font.init()
            font = pygame.font.SysFont("Agency FB", text_size)
            text = font.render(self.text, 1, text_color)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    # Use method to be an interactive button
    '''The position parameter is the positon of the mouse, use 'position = pygame.mouse.get_pos()' 
        in game loop to keep track of the position of the mouse. Also must create an event when
        the mouse clicks the button it creates an action.'''
    def interactive(self, position):
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True
        return False


