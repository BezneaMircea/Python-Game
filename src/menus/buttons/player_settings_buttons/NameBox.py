import pygame
import time

from utils.constants.MenuConstants import *
from utils.pictures.buttons_pictures import NAMEBOX_PNG
from utils.fonts.Fonts import PRESS_START_2P
from utils.colors.Colors import CYAN
from game.GameSetup import currentGameSettings
from utils.RectButton import RectButton

VALID_CHARACTERS = "abcdefghijklmnopqrstuvwxyz0123456789"
WAS_WRITTEN = [False] * len(VALID_CHARACTERS)

class NameBox(RectButton):
    def __init__(self, screen, xPos, yPos, image, text, font, color, interactColor, ownerId):
        super().__init__(screen, xPos, yPos, image)
        self.addTextToButton(text, font, color, interactColor)
        self.ownerId = ownerId
        self.isPressed = False
        self.maxlen = 11
        #currentGameSettings.changePlayerName(self.ownerId, self.text)
    
    
    def performAction(self, mouseCoord, pressed):
        keys = pygame.key.get_pressed()  # Returns a list of all keys
        if (self.isCursorOn(mouseCoord) and pressed[0]):
            self.isPressed = True
        elif pressed[0] or keys[pygame.K_RETURN]:
            self.isPressed = False
        if self.isPressed:
            self.writing(keys)

    
    def interactWithCursor(self, mouseCoord):
        if (self.isCursorOn(mouseCoord) or self.isPressed):
            auxColor = self.color
            self.changeTextColor(self.interactColor)
            self.color = auxColor
        else:
            self.changeTextColor(self.color)
    
    def writing(self, keys):
        global VALID_CHARACTERS
        global WAS_WRITTEN
        if keys[pygame.K_BACKSPACE]:
            self.changeButtonText(self.text[:-1])
            return
        
        for char in VALID_CHARACTERS:
            
            if keys[getattr(pygame, f"K_{char}")] and not WAS_WRITTEN[VALID_CHARACTERS.index(char)]:  # Check for lowercase letter
                self.changeButtonText(self.text + char)
                WAS_WRITTEN[VALID_CHARACTERS.index(char)] = True
                return


font = pygame.font.Font(PRESS_START_2P, 25)
nameBoxPlayerOne = NameBox(SCREEN, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, NAMEBOX_PNG, "Player One", font, (255, 255, 255), CYAN, 1)
nameBoxPlayerTwo = NameBox(SCREEN, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, NAMEBOX_PNG, "Player One", font, (255, 255, 255), CYAN, 2)

__all__ = ['nameBoxPlayerOne', 'nameBoxPlayerTwo']