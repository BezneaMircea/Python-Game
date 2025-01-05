import pygame

class ControlBar():
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
        self.isPressed = False

    def drawButton(self):
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
        self.changeValueToText()
        
    def computeValue(self):
        pass
    
    def changeValueToText(self):
        pass

    def interactWithCursor(self, mouseCoord):
        pass

    def performAction(self, mouseCoord):
        pressedMouse = pygame.mouse.get_pressed()
        if (self.barButton.isCursorOn(mouseCoord) and pressedMouse[0]):
            self.isPressed = True
        
        if not pressedMouse[0]:
            self.isPressed = False
        
        if self.isPressed:
            self.move(mouseCoord)
        
    
    
        
__all__ = ['ControlBar']
