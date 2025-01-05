import pygame

from utils.pictures.buttons_pictures import BUTTON_PNG
from utils.pictures.menu_pictures import BACK_GROUND_JPEG
from menus.PlayerMenu import PlayerMenu, playerOneMenuTitle, playerTwoMenuTitle
from menus.buttons.general_buttons.back import backButton
from menus.buttons.player_settings_buttons.PaddleSelect import paddleSelectOne, paddleSelectTwo
from menus.buttons.player_settings_buttons.PlayerSettingsBorders import playerSettingsBorders
from menus.buttons.player_settings_buttons.NameBox import nameBoxPlayerOne, nameBoxPlayerTwo
from menus.buttons.general_buttons.swipeButtons import (
    swipeLeftButtonPlayerSettingsTwo,
    swipeRightButtonPlayerSettingsTwo,
    swipeLeftButtonPlayerSettingsOne,
    swipeRightButtonPlayerSettingsOne
)

from utils.constants.MenuConstants import *
from utils.colors.Colors import YELLOW, CYAN
from utils.fonts.Fonts import PRESS_START_2P
from utils.RectButton import RectButton

class PlayerButton(RectButton):
    def __init__(self, screen, xPos, yPos, image, playerId):
        super().__init__(screen, xPos, yPos, image)
        self.playerId = playerId
        rectButtonsPlayerMenu, textButtonsPlayerMenu = self.returnPlayerButtonsById()
        self.playerMenu = PlayerMenu(rectButtonsPlayerMenu, textButtonsPlayerMenu, BACK_GROUND_JPEG)
        
    def returnPlayerButtonsById(self):
        if (self.playerId == 1):
            return [paddleSelectOne,
                    swipeLeftButtonPlayerSettingsOne,
                    swipeRightButtonPlayerSettingsOne,
                    backButton,
                    playerSettingsBorders,
                    nameBoxPlayerOne], [playerOneMenuTitle]
        else:
            return [paddleSelectTwo,
                    swipeLeftButtonPlayerSettingsTwo,
                    swipeRightButtonPlayerSettingsTwo,
                    backButton,
                    playerSettingsBorders,
                    nameBoxPlayerTwo], [playerTwoMenuTitle]


    def performAction(self, mouseCoord, pressed):
        if (self.isCursorOn(mouseCoord) and pressed[0]):
            self.playerMenu.startMenu()


playerOneText = "Player One"
xPosPlayerOne = SCREEN_HEIGHT - (SCREEN_HEIGHT) / 10 - 3.5 * DISTANCE_BEETWEEN_BUTTONS
yPosPlayerOne = SCREEN_WIDTH / 2 - 350
playerOneColour = YELLOW
fontPlayerOne = pygame.font.Font(PRESS_START_2P, 18)

playerOneButton = PlayerButton(SCREEN, xPosPlayerOne, yPosPlayerOne, BUTTON_PNG, 1)
playerOneButton.addTextToButton(playerOneText, fontPlayerOne, playerOneColour, CYAN)



playerTwoText = "Player Two"
xPosPlayerTwo = SCREEN_HEIGHT - (SCREEN_HEIGHT) / 10 - 3.5 * DISTANCE_BEETWEEN_BUTTONS
yPosPlayerTwo = SCREEN_WIDTH / 2 + 350
playerTwoColour = YELLOW
fontPlayerTwo = pygame.font.Font(PRESS_START_2P, 18)

playerTwoButton = PlayerButton(SCREEN, xPosPlayerTwo, yPosPlayerTwo, BUTTON_PNG, 2)
playerTwoButton.addTextToButton(playerTwoText, fontPlayerTwo, playerTwoColour, CYAN)

__all__ = ['playerOneButton, playerTwoButton']