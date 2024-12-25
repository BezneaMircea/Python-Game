import pygame


class TextButton():
    def __init__(self, screen, xPos, yPos, text, font, fontSize, fontColour):
        self.screen = screen
        self.xPos = xPos
        self.yPos = yPos
        self.text = text
        self.loadedFont = pygame.font.Font(font, fontSize)
        self.fontColour = fontColour
        self.textSurface = self.loadedFont.render(text, True, fontColour)
        self.textRect = self.textSurface.get_rect(center=(yPos, xPos))

    
    def changeText(self, newText):
        self.text = newText
        self.textSurface = self.loadedFont.render(newText, True, self.fontColour)
        self.textRect = self.textSurface.get_rect(center=(self.yPos, self.xPos))
    
    def displayText(self):
        self.screen.blit(self.textSurface, self.textRect)
            
