from menus.buttons.start_buttons.Setting import settingsButton
from utils.pictures.menu_pictures import BACK_GROUND_JPEG


from utils.constants.MenuConstants import *
from menus.StartMenu import StartMenu
from menus.buttons.start_buttons.Quit import *
from menus.buttons.start_buttons.PlayerTwo import *
from menus.buttons.start_buttons.PlayerOne import *
from menus.buttons.start_buttons.Play import *

from menus.StartMenu import startMenuText


class Game():
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
    
    def start(self):
        rectButtonsStartMenu = [quitButton, playButton, settingsButton,
                                playerOneButton, playerTwoButton]
        titleStartMenuButtons = [startMenuText]
        startMenu = StartMenu(rectButtonsStartMenu, titleStartMenuButtons, BACK_GROUND_JPEG)
        startMenu.startMenu()



myGame = Game(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)
myGame.start()