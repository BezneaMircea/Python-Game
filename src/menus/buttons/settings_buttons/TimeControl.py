import pygame
from utils.pictures.buttons_pictures import BARA_PNG, SCROLL_BUTTON_PNG
from utils.constants.MenuConstants import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.colors.Colors import *
from game.GameSettup import currentGameSettings
from utils.RectButton import RectButton
from utils.TextButton import TextButton
import math

X_POS = SCREEN_HEIGHT / 4
Y_POS = SCREEN_WIDTH / 2


bar = RectButton(SCREEN, X_POS, Y_POS, BARA_PNG)
barButton = RectButton(SCREEN, X_POS, Y_POS, SCROLL_BUTTON_PNG)
textButton = TextButton(SCREEN, X_POS, Y_POS - 320, "Time:", PRESS_START_2P, 30, CYAN)
valueButton = TextButton(SCREEN, X_POS, Y_POS + 320, "02:30", PRESS_START_2P, 20, CYAN)



class TimeControl():
    # originalValue should be given as seconds if we are talking about time
    def __init__(self, bar, barButton, textButton, leftMax,
                 rightMax, valueButton, originalValue, maxValue, minValue):
        self.bar = bar
        self.barButton = barButton
        self.textButton = textButton
        self.leftMax = leftMax
        self.rightMax = rightMax
        self.valueButton = valueButton
        self.originalPos = barButton.yPos
        self.originalValue = originalValue
        self.currentValue = originalValue
        self.maxValue = maxValue
        self.minValue = minValue
        self.unit = (maxValue - minValue) / (rightMax - leftMax)

    def draw(self):
        self.bar.drawButton()
        self.barButton.drawButton()
        self.textButton.displayText()
        self.valueButton.displayText()
    
    def move(self, mouseCoord):
        newY = mouseCoord[0]
        if newY > self.rightMax:
            newY = self.rightMax
            
        
        if newY < self.leftMax:
            newY = self.leftMax
    
        self.barButton.changePosition(self.barButton.xPos, newY)
        self.changeTextToValue()
    
    def changeTextToValue(self):
        self.computeValue()
        minutes = math.floor(self.currentValue / 60)
        seconds = self.currentValue % 60
        if seconds < 10:
            self.valueButton.changeText(f"0{minutes}:0{seconds}")
        else:
            self.valueButton.changeText(f"0{minutes}:{seconds}")
    
    def computeValue(self):
        self.currentValue = self.originalValue + round((self.unit * (self.barButton.yPos - self.originalPos)))
        currentGameSettings.time = self.currentValue
            

        
timeControl = TimeControl(bar, barButton, textButton, Y_POS - 230, Y_POS + 230, valueButton, 150, 240, 60)

__all__ = ['timeControl']