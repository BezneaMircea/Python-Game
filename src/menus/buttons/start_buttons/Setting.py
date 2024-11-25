import pygame

from utils.pictures.buttons_pictures import *

from utils.colors.Colors import YELLOW
from utils.constants.MenuConstants import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.constants.MenuConstants import SCREEN
from utils.RectButton import RectButton

textSettings = "Settings"
xPosSettings = SCREEN_HEIGHT - (SCREEN_HEIGHT) / 10 - DISTANCE_BEETWEEN_BUTTONS
yPosSettings = SCREEN_WIDTH / 2
fontSettings = pygame.font.Font(PRESS_START_2P, 24)
colorSettings = YELLOW
settingsButton = RectButton(screen=SCREEN, xPos=xPosSettings, yPos=yPosSettings, image=BUTTON_PNG)
settingsButton.addTextToButton(textSettings, fontSettings, colorSettings)

__all__ = ['settingsButton']