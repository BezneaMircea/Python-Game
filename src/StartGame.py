from utils.constants.MenuConstants import *
from menus.StartMenu import StartMenu
from menus.buttons.start_buttons.Quit import *
from menus.buttons.start_buttons.PlayerTwo import *
from menus.buttons.start_buttons.PlayerOne import *
from menus.buttons.start_buttons.Play import *
from menus.buttons.start_buttons.Setting import *


class Game():
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
    
    def start(self):
        rectButtonsStartMenu = [quitButton, settingsButton, playButton,
                                playerOneButton, playerTwoButton]
        startMenu = StartMenu(SCREEN, rectButtonsStartMenu, None)
        startMenu.startMenuLoop()
        
myGame = Game(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)
myGame.start()