import pygame
from utils.constants.MenuConstants import *

class Menu():
    """ Constructor for the menu class. rectButtons and
        textButtons are a lists of RectButtons and TextButtons
        (see utils) 
    """
    def __init__(self, rectButtons, textButtons):
        self.rectButtons = rectButtons
        self.textButtons = textButtons
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
            textButton.drawButton()
            
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
    
    def addButton(self, button):
        self.rectButtons.insert(0, button)
        
        
    # def menuLoop(self):
    #             while self.running:

    #         SCREEN.blit(BACK_GROUND_JPEG, (0, 0))
    #         SCREEN.blit(titleSurface, titleRect)    
            
    #         for event in pygame.event.get():        
                
    #             if event.type == pygame.QUIT:
    #                 self.running = False
                
    #             mouseCoord = pygame.mouse.get_pos()
    #             super().buttonsInteractions(mouseCoord)

    #             pressed = pygame.mouse.get_pressed()
    #             self.performButtonActions(mouseCoord, pressed)

    #                     # if (settingsButton.isCursorOn(mouseCoord)):
    #                     #     pass 
    #                     #     # settingsMenu()
                    

    #                     # if (playerOneButton.isCursorOn(mouseCoord)):
    #                     #     pass 
    #                     #     # playerMenu("Player One", 1)
                        
    #                     # if (playerTwoButton.isCursorOn(mouseCoord)):
    #                     #     pass 
    #                     #     # playerMenu("Player Two", 2)

    #         super().drawAllButtons()
            

    #         pygame.display.update()  
                
    #     pygame.quit()