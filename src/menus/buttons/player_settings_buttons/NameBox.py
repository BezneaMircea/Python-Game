import pygame
import time

from utils.RectButton import RectButton
from utils.constants.MenuConstants import *
from utils.fonts.Fonts import *
from game.Player import *

class Boxes:
    def __init__(self, boxPlayerOne, boxPlayerTwo):
        self.boxPlayerOne = boxPlayerOne
        self.boxPlayerTwo = boxPlayerTwo

    def write(self, event, playerId):
        if playerId == 1:
            self.boxPlayerOne.write(event)
            playerOne.name = self.boxPlayerOne.text
        if playerId == 2:
            self.boxPlayerTwo.write(event)
            playerTwo.name = self.boxPlayerTwo.text

    def processHeldKeys(self, playerId):
        if playerId == 1:
            self.boxPlayerOne.processHeldKeys()
        if playerId == 2:
            self.boxPlayerTwo.processHeldKeys()

    def draw(self, playerId):
        if playerId == 1:
            self.boxPlayerOne.draw()
        if playerId == 2:
            self.boxPlayerTwo.draw()

# Class to manage individual text boxes for player names
class NameBox(RectButton):
    def __init__(self, screen, xPos, yPos, image, font, text, textColour, maxChars):
        super().__init__(screen, xPos, yPos, image)

        self.font = font
        self.text = text
        self.textColout = textColour
        self.maxChars = maxChars
        self.active = False
        self.cursorVisible = True
        self.lastBlinkTime = time.time()
        self.cursorPos = len(text)
        self.lastKeyTime = 0  # To control the repeat rate
        self.keyRepeatInterval = 0.2  # Seconds between key repeats

    def write(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the name box
            self.active = self.rect.collidepoint(event.pos)
        
        if event.type == pygame.KEYDOWN and self.active:
            self.processKey(event.key, event.unicode)

    def processKey(self, key, unicode):
        """Handles text modification when a key is pressed."""
        if key == pygame.K_BACKSPACE:
            if self.cursorPos > 0:
                self.text = self.text[:self.cursorPos - 1] + self.text[self.cursorPos:]
                self.cursorPos -= 1
        elif key == pygame.K_LEFT:
            self.cursorPos = max(0, self.cursorPos - 1)
        elif key == pygame.K_RIGHT:
            self.cursorPos = min(len(self.text), self.cursorPos + 1)
        elif key == pygame.K_DELETE:
            if self.cursorPos < len(self.text):
                self.text = self.text[:self.cursorPos] + self.text[self.cursorPos + 1:]
        else:
            self.text = self.text[:self.cursorPos] + unicode + self.text[self.cursorPos:]
            self.cursorPos += 1

        # Adjust the offset if the text is too long
        self.adjustOffset()

    def adjustOffset(self):
        textWidth = self.font.size(self.text[:self.cursorPos])[0]
        if textWidth - self.offset > self.rect.width - 10:  # 10 pixels padding
            self.offset = textWidth - (self.rect.width - 10)
        elif textWidth < self.offset:
            self.offset = textWidth

    def processHeldKeys(self):
        """Processes continuous input by checking pressed keys."""
        if self.active:
            keys = pygame.key.get_pressed()
            currentTime = time.time()

            if currentTime - self.lastKeyTime > self.keyRepeatInterval:
                if keys[pygame.K_BACKSPACE]:
                    self.processKey(pygame.K_BACKSPACE, '')
                elif keys[pygame.K_LEFT]:
                    self.processKey(pygame.K_LEFT, '')
                elif keys[pygame.K_RIGHT]:
                    self.processKey(pygame.K_RIGHT, '')
                elif keys[pygame.K_DELETE]:
                    self.processKey(pygame.K_DELETE, '')

                self.lastKeyTime = currentTime

    def draw(self):
        # Draw the background
        pygame.draw.rect(self.screen, self.bgColor, self.rect)
        # Draw the border
        pygame.draw.rect(self.screen, self.bgColor, self.rect, 2)
        
        # Render the visible portion of the text
        textSurface = self.font.render(self.text, True, self.color)
        textWidth, textHeight = self.font.size(self.text)

        # Create a surface for the visible text
        visibleTextSurface = pygame.Surface((self.rect.width - 10, self.rect.height), pygame.SRCALPHA)
        visibleTextSurface.fill((0, 0, 0, 0))  # Make the surface transparent
        visibleTextSurface.blit(textSurface, (-self.offset, 0))
        self.screen.blit(visibleTextSurface, (self.rect.x + 5, self.rect.y + (self.rect.height - textHeight) // 2))

        # Blink cursor is active
        if self.active:
            currentTime = time.time()
            if currentTime - self.lastBlinkTime > 0.3: # 0.5 secunde between blinks
                self.cursorVisible = not self.cursorVisible
                self.lastBlinkTime = currentTime
            
            if self.cursorVisible:
                cursorX = self.rect.x + 5 + self.font.size(self.text[:self.cursorPos])[0] - self.offset
                if self.rect.x + 5 <= cursorX <= self.rect.x + self.rect.width - 5:
                    pygame.draw.line(self.screen, self.color,
                                     (cursorX, self.rect.y + 5),
                                     (cursorX, self.rect.y + self.rect.height - 5), 2)
                    

fontNameBox = pygame.font.Font(PRESS_START_2P, 24)

nameInputBoxPlayerOne = NameBox(SCREEN, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 50, fontNameBox, text=f'Player 1')
nameInputBoxPlayerTwo = NameBox(SCREEN, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 50, fontNameBox, text=f'Player 2')

nameBoxes = Boxes(nameInputBoxPlayerOne, nameInputBoxPlayerTwo)

__all__ = ['nameBoxes']