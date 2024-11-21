import pygame

from utils.colors.Colors import YELLOW
from utils.constants.MenuConstants import *
from utils.pictures.Pictures import BUTTON_PNG
from utils.fonts.Fonts import PRESS_START_2P
from utils.constants.MenuConstants import SCREEN
from utils.RectButton import RectButton

playerOneText = "Player One"
xPosPlayerOne = SCREEN_HEIGHT - (SCREEN_HEIGHT) / 10 - 3.5 * DISTANCE_BEETWEEN_BUTTONS
yPosPlayerOne = SCREEN_WIDTH / 2 - 350
playerOneColour = YELLOW
fontPlayerOne = pygame.font.Font(PRESS_START_2P, 18)

playerOneButton = RectButton(SCREEN, xPosPlayerOne, yPosPlayerOne, BUTTON_PNG)
playerOneButton.addTextToButton(playerOneText, fontPlayerOne, playerOneColour)

__all__ = ['playerOneButton']