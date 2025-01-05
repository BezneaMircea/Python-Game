class Menu():
    """ Constructor for the menu class. rectButtons and
        textButtons are a lists of RectButtons and TextButtons
        (see utils) 
    """
    def __init__(self, rectButtons, textButtons):
        self.rectButtons = rectButtons
        self.textButtons = textButtons

    def drawAllRectButtons(self):
        if self.rectButtons == None:
            return

        for rectButton in self.rectButtons:
            rectButton.drawButton()
            
    def drawAllTextButtons(self):
        if self.textButtons == None:
            return

        for textButton in self.textButtons:
            textButton.drawButton()
            
    def drawAllButtons(self):
        self.drawAllRectButtons()
        self.drawAllTextButtons()

    def buttonsInteractions(self, mouseCoord):
        for rectButton in self.rectButtons:
            rectButton.interactWithCursor(mouseCoord)
    
    def performButtonActions(self, mouseCoord):
        for rectButton in self.rectButtons:
            rectButton.performAction(mouseCoord)