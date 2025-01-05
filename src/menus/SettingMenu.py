from menus.Menu import Menu
from utils.TextButton import TextButton
from utils.constants.MenuConstants import *
from utils.colors.Colors import *
from utils.fonts.Fonts import *
from utils.pictures.menu_pictures import *



settingsMenuText = TextButton(SCREEN, SCREEN_HEIGHT / 10, SCREEN_WIDTH / 2,
                              "Game Settings", PRESS_START_2P, 70, YELLOW)


class SettingsMenu(Menu):
    def __init__(self, rectButtons, textButtons, backgroundPicture):
        super().__init__(rectButtons, textButtons, backgroundPicture)
