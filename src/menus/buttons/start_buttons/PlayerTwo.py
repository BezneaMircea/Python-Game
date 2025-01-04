import pygame

from utils.pictures.buttons_pictures import *

from utils.colors.Colors import YELLOW, CYAN
from utils.constants.MenuConstants import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.constants.MenuConstants import SCREEN
from utils.RectButton import RectButton

playerTwoText = "Player Two"
xPosPlayerTwo = SCREEN_HEIGHT - (SCREEN_HEIGHT) / 10 - 3.5 * DISTANCE_BEETWEEN_BUTTONS
yPosPlayerTwo = SCREEN_WIDTH / 2 + 350
playerTwoColour = YELLOW
fontPlayerTwo = pygame.font.Font(PRESS_START_2P, 18)

playerTwoButton = RectButton(SCREEN, xPosPlayerTwo, yPosPlayerTwo, BUTTON_PNG)
playerTwoButton.addTextToButton(playerTwoText, fontPlayerTwo, playerTwoColour, CYAN)

__all__ = ['playerTwoButton']