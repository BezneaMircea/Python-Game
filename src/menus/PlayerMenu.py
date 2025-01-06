from menus.Menu import Menu
from utils.TextButton import TextButton
from utils.constants.MenuConstants import *
from utils.colors.Colors import *
from utils.fonts.Fonts import *



playerOneMenuTitle = TextButton(SCREEN, SCREEN_HEIGHT / 10, SCREEN_WIDTH / 2,
                                "Player One", PRESS_START_2P, 70, YELLOW)
playerTwoMenuTitle = TextButton(SCREEN, SCREEN_HEIGHT / 10, SCREEN_WIDTH / 2,
                                "Player Two", PRESS_START_2P, 70, YELLOW)

class PlayerMenu(Menu):
    def __init__(self, rectButtons, textButtons, backGroundPicture):
        super().__init__(rectButtons, textButtons, backGroundPicture)
