
"""Class used to create a rectangular
   button and it s methods
"""
class RectButton():
    def __init__(self, screen, xPos, yPos, image):
        """Constructor for the button class
        
        Args:
            screen (pygame.Surface) the screen where the button belongs
            xPos (float): the x coord of the center
            yPos (float): the y coord of the center
            path (String): path to the picture that represent the button
        """
        self.screen = screen
        self.xPos = xPos
        self.yPos = yPos
        self.image = image
        self.imageRect = self.image.get_rect(center=(yPos, xPos))
    
    def isCursorOn(self, coords):
        """Method to check if mouse cursor is on button

        Args:
            coords (tuple(x, y)): coords of the mouse cursor
            

        Returns:
            boolean: true if cursor is on the button, false otherwise 
        """
        x, y = coords
        return self.imageRect.collidepoint(x, y)

    
    def drawButton(self):
        """ Method used to drow the button and it s text
        """
        self.screen.blit(self.image, self.imageRect)
        try:
            self.screen.blit(self.textSurface, self.textRect)
        except:
            pass
            
    def changeTextColor(self, color):
        self.color = color
        textSurface = self.font.render(self.text, True, color)
        textRect = textSurface.get_rect(center=self.imageRect.center)
        self.textSurface = textSurface
        self.textRect = textRect
    
    
    def addTextToButton(self, text, font, color, interactColor):
        """ Method used to add text in a button

        Args:
            text (String): text to add
            font (pygame.font.Font): the font 
            color (tuple (r, g, b)): color of text
        """
        self.text = text
        self.color = color
        self.font = font
        self.interactColor = interactColor
        
        textSurface = font.render(text, True, color)
        textRect = textSurface.get_rect(center=self.imageRect.center)
        self.textSurface = textSurface
        self.textRect = textRect
    
    def changeButtonText(self, newText):
        self.text = newText
        self.textSurface = self.font.render(newText, True, self.color)
        self.textRect = self.textSurface.get_rect(center=self.imageRect.center)

    def changePosition(self, newXPos, newYPos):
        self.xPos = newXPos
        self.yPos = newYPos
        self.imageRect = self.image.get_rect(center=(newYPos, newXPos))
    
    def changeButtonImg(self, image):
        self.image = image
        self.imageRect = self.image.get_rect(center=(self.yPos, self.xPos))

        
    def interactWithCursor(self, mouseCoord):
        if (self.isCursorOn(mouseCoord)):
            auxColor = self.color
            self.changeTextColor(self.interactColor)
            self.color = auxColor
        else:
            self.changeTextColor(self.color)
    
    """ This method is used to perform a button action
        Some buttons may quit a menu, (e.g. Quit, EXIT, BACK)
        So the return value of this function is the current state
        of the menu that owns the button (stop = True or stop = False)
    """
    def performAction(self, mouseCoord, pressed):
        return False