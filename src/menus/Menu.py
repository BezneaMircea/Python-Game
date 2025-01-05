import pygame
from utils.constants.MenuConstants import *

class Menu():
    """ Constructor for the menu class. rectButtons and
        textButtons are a lists of RectButtons and TextButtons
        (see utils) 
    """
    def __init__(self, rectButtons, textButtons, backGroundPicture):
        self.rectButtons = rectButtons
        self.textButtons = textButtons
        self.backGroundPicture = backGroundPicture
        self.running = True

    def drawAllRectButtons(self):
        if self.rectButtons == None:
            return

        for rectButton in self.rectButtons:
            rectButton.drawButton()
            
    def drawAllTextButtons(self):
        if self.textButtons == None:
            return

        for textButton in self.textButtons:
            textButton.displayText()
            
    def drawAllButtons(self):
        self.drawAllRectButtons()
        self.drawAllTextButtons()

    def buttonsInteractions(self, mouseCoord):
        for rectButton in self.rectButtons:
            rectButton.interactWithCursor(mouseCoord)
    
    def performButtonActions(self, mouseCoord, pressed):
        for rectButton in self.rectButtons:
            stop = rectButton.performAction(mouseCoord, pressed)
            if stop:
                self.stopMenu()

    def stopMenu(self):
        self.running = False
    
    def startMenu(self):
        self.running = True
        self.menuLoop()
    
    def menuLoop(self):
        while self.running:

            SCREEN.blit(self.backGroundPicture, (0, 0))  
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                
                mouseCoord = pygame.mouse.get_pos()
                pressed = pygame.mouse.get_pressed()
                
                self.buttonsInteractions(mouseCoord)
                self.performButtonActions(mouseCoord, pressed)
            
            self.drawAllButtons()
            pygame.display.update()  
