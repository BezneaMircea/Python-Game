import pygame
import time

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

    def draw(self, playerId):
        if playerId == 1:
            self.boxPlayerOne.draw()
        if playerId == 2:
            self.boxPlayerTwo.draw()

# Class to manage individual text boxes for player names
class NameBox:
    def __init__(self, screen, x, y, width, height, font, text='', color=(255, 255, 255), bg_color=(0, 0, 0), border_color=(200, 200, 200)):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.text = text
        self.color = color
        self.bg_color = bg_color
        self.border_color = border_color
        self.active = False
        self.offset = 0  # Offset for the blinking cursor
        self.cursor_visible = True
        self.last_blink_time = time.time()
        self.cursor_pos = len(text)

    def write(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the name box
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:self.cursor_pos - 1] + self.text[self.cursor_pos:]
                self.cursor_pos = max(0, self.cursor_pos - 1)
            elif event.key == pygame.K_LEFT:
                self.cursor_pos = max(0, self.cursor_pos - 1)
            elif event.key == pygame.K_RIGHT:
                self.cursor_pos = min(len(self.text), self.cursor_pos + 1)
            elif event.key == pygame.K_DELETE:
                self.text = self.text[:self.cursor_pos] + self.text[self.cursor_pos + 1:]
            else:
                self.text = self.text[:self.cursor_pos] + event.unicode + self.text[self.cursor_pos:]
                self.cursor_pos += 1

            # Adjust the offset if the text is too long
            self.adjust_offset()

    def adjust_offset(self):
        text_width = self.font.size(self.text[:self.cursor_pos])[0]
        if text_width - self.offset > self.rect.width - 10:  # 10 pixels padding
            self.offset = text_width - (self.rect.width - 10)
        elif text_width < self.offset:
            self.offset = text_width

    def draw(self):
        # Draw the background
        pygame.draw.rect(self.screen, self.bg_color, self.rect)
        # Draw the border
        pygame.draw.rect(self.screen, self.border_color, self.rect, 2)
        
        # Render the visible portion of the text
        text_surface = self.font.render(self.text, True, self.color)
        text_width, text_height = self.font.size(self.text)

        # Create a surface for the visible text
        visible_text_surface = pygame.Surface((self.rect.width - 10, self.rect.height), pygame.SRCALPHA)
        visible_text_surface.fill((0, 0, 0, 0))  # Make the surface transparent
        visible_text_surface.blit(text_surface, (-self.offset, 0))
        self.screen.blit(visible_text_surface, (self.rect.x + 5, self.rect.y + (self.rect.height - text_height) // 2))

        # Blink cursor is active
        if self.active:
            current_time = time.time()
            if current_time - self.last_blink_time > 0.3: # 0.5 secunde between blinks
                self.cursor_visible = not self.cursor_visible
                self.last_blink_time = current_time
            
            if self.cursor_visible:
                cursor_x = self.rect.x + 5 + self.font.size(self.text[:self.cursor_pos])[0] - self.offset
                if self.rect.x + 5 <= cursor_x <= self.rect.x + self.rect.width - 5:
                    pygame.draw.line(self.screen, self.color,
                                     (cursor_x, self.rect.y + 5),
                                     (cursor_x, self.rect.y + self.rect.height - 5), 2)
                    

fontNameBox = pygame.font.Font(PRESS_START_2P, 24)

nameInputBoxPlayerOne = NameBox(SCREEN, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 50, fontNameBox, text=f'Player 1')
nameInputBoxPlayerTwo = NameBox(SCREEN, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 50, fontNameBox, text=f'Player 2')

nameBoxes = Boxes(nameInputBoxPlayerOne, nameInputBoxPlayerTwo)

__all__ = ['nameBoxes']