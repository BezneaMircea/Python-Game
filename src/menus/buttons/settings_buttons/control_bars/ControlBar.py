# This is a global variable for control bars. Obviously
# only one control bar should move at a time.
# Introduced to fix the case where left mouse button is pressed
# a bar is selected and then cursor is dragged to another bar
# resuling in both bars to be pressed simultaniously.
OTHER_CONTROL_BAR_IN_USE = False

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

    def performAction(self, mouseCoord, pressed):
        global OTHER_CONTROL_BAR_IN_USE
        if (self.barButton.isCursorOn(mouseCoord) and pressed[0] and not OTHER_CONTROL_BAR_IN_USE):
            self.isPressed = True
            OTHER_CONTROL_BAR_IN_USE = True
        
        if not pressed[0]:
            if self.isPressed:
                OTHER_CONTROL_BAR_IN_USE = False
            
            self.isPressed = False
        
        if self.isPressed:
            self.move(mouseCoord)
        
    
    
        
__all__ = ['ControlBar']
