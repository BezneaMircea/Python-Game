import pygame


from utils.pictures.buttons_pictures import *

from utils.colors.Colors import YELLOW
from utils.constants.MenuConstants import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.constants.MenuConstants import SCREEN
from utils.RectButton import RectButton

playText = 'Play'
xPosPlay = SCREEN_HEIGHT - (SCREEN_HEIGHT) / 10 - 2 * DISTANCE_BEETWEEN_BUTTONS
yPosPlay = SCREEN_WIDTH / 2
playColour = YELLOW
playFont = pygame.font.FontType(PRESS_START_2P, 35)

playButton = RectButton(SCREEN, xPosPlay, yPosPlay, BUTTON_PNG)
playButton.addTextToButton(playText, playFont, playColour)


__all__ = ['playButton']