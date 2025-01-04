import pygame

from utils.pictures.buttons_pictures import *

from utils.colors.Colors import YELLOW, CYAN
from utils.constants.MenuConstants import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.constants.MenuConstants import SCREEN
from utils.RectButton import RectButton

from menus.SettingMenu import settingsMenu

class SettingButton(RectButton):
    def __init__(screen, xPos, yPos, image):
        super().__init__(screen, xPos, yPos, image)
        
    def performAction():
        settingsMenu()
        


textSettings = "Settings"
xPosSettings = SCREEN_HEIGHT - (SCREEN_HEIGHT) / 10 - DISTANCE_BEETWEEN_BUTTONS
yPosSettings = SCREEN_WIDTH / 2
fontSettings = pygame.font.Font(PRESS_START_2P, 24)
colorSettings = YELLOW
settingsButton = RectButton(screen=SCREEN, xPos=xPosSettings, yPos=yPosSettings, image=BUTTON_PNG)
settingsButton.addTextToButton(textSettings, fontSettings, colorSettings, CYAN)

__all__ = ['settingsButton']