import pygame

from utils.constants.MenuConstants import *
from utils.pictures.buttons_pictures import *
from utils.pictures.menu_pictures import BACK_GROUND_JPEG
from menus.SettingMenu import SettingsMenu

from utils.colors.Colors import YELLOW, CYAN
from utils.fonts.Fonts import PRESS_START_2P
from utils.constants.MenuConstants import SCREEN
from utils.RectButton import RectButton

from menus.buttons.general_buttons.back import backButton
from menus.buttons.settings_buttons.MapSelect import mapSelection
from menus.buttons.general_buttons.swipeButtons import swipeRightButton, swipeLeftButton
from menus.buttons.settings_buttons.Borders import mapSelectionBorders
from menus.buttons.settings_buttons.control_bars.TimeControl import timeControl
from menus.buttons.settings_buttons.control_bars.VolumeControl import volumeControl

from menus.SettingMenu import settingsMenuText



class SettingButton(RectButton):
    def __init__(self, screen, xPos, yPos, image):
        super().__init__(screen, xPos, yPos, image)
        rectButtonsSettingsMenu = [swipeRightButton, swipeLeftButton,
                                   mapSelection, mapSelectionBorders,
                                   timeControl, volumeControl, backButton]
        textButtonsSettingsMenu = [settingsMenuText]
        self.settingsMenu = SettingsMenu(rectButtonsSettingsMenu, textButtonsSettingsMenu, BACK_GROUND_JPEG)
        
        
    def performAction(self, mouseCoord, pressed):
        if self.isCursorOn(mouseCoord) and pressed[0]:
            self.settingsMenu.startMenu()
        
    

textSettings = "Settings"
xPosSettings = SCREEN_HEIGHT - (SCREEN_HEIGHT) / 10 - DISTANCE_BEETWEEN_BUTTONS
yPosSettings = SCREEN_WIDTH / 2
fontSettings = pygame.font.Font(PRESS_START_2P, 24)
colorSettings = YELLOW
settingsButton = SettingButton(SCREEN, xPosSettings, yPosSettings, BUTTON_PNG)
settingsButton.addTextToButton(textSettings, fontSettings, colorSettings, CYAN)

__all__ = ['settingButton']