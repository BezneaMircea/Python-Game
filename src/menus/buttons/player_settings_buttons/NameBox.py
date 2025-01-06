import pygame
import time

from utils.constants.MenuConstants import *
from utils.pictures.buttons_pictures import NAMEBOX_PNG
from utils.fonts.Fonts import PRESS_START_2P
from utils.colors.Colors import CYAN, YELLOW
from game.GameSetup import currentGameSettings
import time
from utils.RectButton import RectButton


class NameBox(RectButton):
    def __init__(self, screen, xPos, yPos, image, cursorImage, text, font, color, interactColor, ownerId):
        super().__init__(screen, xPos, yPos, image)
        self.addTextToButton(text, font, color, interactColor)
        self.ownerId = ownerId
        self.isPressed = False
        self.maxlen = 11
        self.validCharaters = "abcdefghijklmnopqrstuvwxyz0123456789 "
        self.was_written = [False] * len(self.validCharaters)
        self.lastReset = time.time()

        # Cursor setup
        self.cursor = RectButton(screen, xPos , yPos + font.size(text)[0] / 2, cursorImage)
        self.cursorVisible = True
        self.cursorLastActive = time.time()

    def resetDictionary(self):
        currentTime = time.time()
        if currentTime - self.lastReset > 0.05:
            self.was_written = [False] * len(self.validCharaters)
            self.lastReset = currentTime

    def performAction(self, mouseCoord, pressed):
        keys = pygame.key.get_pressed()

        if self.isCursorOn(mouseCoord) and pressed[0]:
            self.isPressed = True
        elif pressed[0] or keys[pygame.K_RETURN]:
            self.isPressed = False
        if self.isPressed:
            self.writing(keys)

    def blinkCursor(self):
        """Toggle cursor visibility for blinking effect."""
        currentTime = time.time()
        # Blink every 0.5 seconds
        if currentTime - self.cursorLastActive > 0.5:
            self.cursorVisible = not self.cursorVisible
            self.cursorLastActive = currentTime

    def drawButton(self):
        """Override to draw text box and cursor."""
        # Draw the text box
        super().drawButton()
        self.blinkCursor()
        if self.cursorVisible and self.isPressed:
            # Draw the cursor only when editing
            self.cursor.drawButton()

    def writing(self, keys):
        """Handles input for text editing."""
        self.resetDictionary()
        currentGameSettings.changePlayerName(self.ownerId, self.text)
        if keys[pygame.K_BACKSPACE]:
            if len(self.text) == 0:
                return

            letterSize = font.size(self.text[-1])[0] / 2

            self.changeButtonText(self.text[:-1])
            self.cursor.changePosition(self.cursor.xPos, self.cursor.yPos - letterSize)
            return

        for char in self.validCharaters:
            if char == " ":
                char = "SPACE"

            if keys[getattr(pygame, f"K_{char}")] and len(self.text) < self.maxlen:
                if char == "SPACE":
                    char = " "

                if not self.was_written[self.validCharaters.index(char)]:
                    self.changeButtonText(self.text + char)
                    self.was_written[self.validCharaters.index(char)] = True
                    self.cursor.changePosition(self.cursor.xPos, self.cursor.yPos + font.size(char)[0] / 2)
                    return


font = pygame.font.Font(PRESS_START_2P, 25)
cursorImage = pygame.Surface((3, font.get_height() + 5))
cursorImage.fill(YELLOW)

nameBoxPlayerOne = NameBox(SCREEN, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, NAMEBOX_PNG, cursorImage, "Player 1", font, (255, 255, 255), CYAN, 1)
nameBoxPlayerTwo = NameBox(SCREEN, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, NAMEBOX_PNG, cursorImage, "Player 2", font, (255, 255, 255), CYAN, 2)

__all__ = ['nameBoxPlayerOne', 'nameBoxPlayerTwo']