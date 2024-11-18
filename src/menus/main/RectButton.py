import pygame

"""Class used to create a rectangular
   button and it s methods
"""
class RectButton():
    def __init__(self, screen, xPos, yPos, path):
        """Constructor for the button class

        Args:
            screen (pygame.Surface) the screen where the button belongs
            x (float): the x coord of the top left corner
            y (float): the y coord of the top left corner
            width (float): the width of the button
            height (float): the height of the button
            color (tuple): RGB type color tuple used in case no image
            provided 
            image (float): the image loaded to represent the button
        """
        self.screen = screen
        self.xPos = xPos
        self.yPos = yPos
        self.image = pygame.image.load(path)
        self.imageRect = self.image.get_rect(topleft=(yPos, xPos))
    
    def isPressed(self, coords):
        """Method to check if mouse cursor is on button

        Args:
            x (float): the current x coord where we are
            y (float): the current y coord where we are

        Returns:
            boolean: true if the button is pressed, false otherwise 
        """
        x, y = coords
        return self.imageRect.collidepoint(x, y)

    
    def drawButton(self):
        self.screen.blit(self.image, self.imageRect)

    
    
        
    