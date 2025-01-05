import pygame


from utils.pictures.buttons_pictures import *
from game.Game import Game
from game.GameSetup import currentGameSettings

from utils.colors.Colors import YELLOW, CYAN
from utils.constants.MenuConstants import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.constants.MenuConstants import SCREEN
from utils.RectButton import RectButton


class Play(RectButton):
    def __init__(self, screen, xPos, yPos, image):
        super().__init__(screen, xPos, yPos, image)
    
    def performAction(self, mouseCoord, pressed):
        if (self.isCursorOn(mouseCoord) and pressed[0]):
            game = Game(currentGameSettings)
            game.start()


playText = 'Play'
xPosPlay = SCREEN_HEIGHT - (SCREEN_HEIGHT) / 10 - 2 * DISTANCE_BEETWEEN_BUTTONS
yPosPlay = SCREEN_WIDTH / 2
playColour = YELLOW
playFont = pygame.font.FontType(PRESS_START_2P, 35)

playButton = Play(SCREEN, xPosPlay, yPosPlay, BUTTON_PNG)
playButton.addTextToButton(playText, playFont, playColour, CYAN)


__all__ = ['playButton']