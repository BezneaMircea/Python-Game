import pygame

from utils.colors.Colors import YELLOW
from utils.constants.MenuConstants import *
from utils.pictures.Pictures import BUTTON_PNG
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
backButton.addTextToButton(backText, fontBack, backColour)

__all__ = ['backButton']
