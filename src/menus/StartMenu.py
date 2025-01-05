from menus.Menu import Menu
from utils.constants.MenuConstants import *
from utils.colors.Colors import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.TextButton import TextButton


startMenuText = TextButton(SCREEN, SCREEN_HEIGHT / 10, SCREEN_WIDTH / 2, 
                           "Air Hockey", PRESS_START_2P, 70, YELLOW)

class StartMenu(Menu):
    def __init__(self, rectButtons, textButtons, backGroundPicture):
        super().__init__(rectButtons, textButtons, backGroundPicture)


   