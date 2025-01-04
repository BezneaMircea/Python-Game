import pygame

from utils.pictures.buttons_pictures import *

from utils.colors.Colors import YELLOW, RED
from utils.constants.MenuConstants import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.constants.MenuConstants import SCREEN
from utils.RectButton import RectButton

"""Button used for Settings, PlayerOne, PlayerTwo menus
"""

backText = 'Back'
xPosBack = SCREEN_HEIGHT - SCREEN_HEIGHT / 10
yPosBack = SCREEN_WIDTH / 2
backColour = YELLOW
fontBack = pygame.font.Font(PRESS_START_2P, 36)

backButton = RectButton(SCREEN, xPosBack, yPosBack, BUTTON_PNG)
backButton.addTextToButton(backText, fontBack, backColour, RED)

__all__ = ['backButton']
