import pygame
from utils.colors.Colors import YELLOW, CYAN
from menus.buttons.start_buttons.Setting import settingsButton
from utils.fonts.Fonts import PRESS_START_2P
from utils.pictures.buttons_pictures import BUTTON_PNG

from utils.constants.MenuConstants import *
from menus.StartMenu import StartMenu
from menus.buttons.start_buttons.Quit import *
from menus.buttons.start_buttons.PlayerTwo import *
from menus.buttons.start_buttons.PlayerOne import *
from menus.buttons.start_buttons.Play import *


class Game():
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
    
    def start(self):
        rectButtonsStartMenu = [quitButton, playButton, settingsButton,
                                playerOneButton, playerTwoButton]
        startMenu = StartMenu(SCREEN, rectButtonsStartMenu, None)
        startMenu.startMenuLoop()



myGame = Game(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)
myGame.start()