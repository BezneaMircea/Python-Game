import pygame

from utils.pictures.buttons_pictures import *

from utils.colors.Colors import YELLOW, RED
from utils.constants.MenuConstants import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.constants.MenuConstants import SCREEN
from utils.RectButton import RectButton

class Quit(RectButton):
    def __init__(self, screen, xPos, yPos, image):
        super().__init__(screen, xPos, yPos, image)
        
    def performAction(self, mouseCoord, pressed):
        if (self.isCursorOn(mouseCoord) and pressed[0]):
            return True


textQuit = "Quit"
xPosQuit = SCREEN_HEIGHT - (SCREEN_HEIGHT) / 10
yPosQuit = SCREEN_WIDTH / 2
fontQuit = pygame.font.Font(PRESS_START_2P, 36)
colorQuit = YELLOW
quitButton = Quit(screen=SCREEN, xPos=xPosQuit, yPos=yPosQuit, image=BUTTON_PNG)
quitButton.addTextToButton(textQuit, fontQuit, colorQuit, RED)

__all__ = ['quitButton']
