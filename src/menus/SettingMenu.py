import pygame

from utils.constants.MenuConstants import *
from utils.colors.Colors import *
from utils.fonts.Fonts import *
from utils.pictures.menu_pictures import *

from buttons.general_buttons.back import *

from game.GameSettup import *



def isCursorOnButtons(mouseCoord):
    if (backButton.isCursorOn(mouseCoord)):
        backButton.changeTextColor(CYAN)
    else:
        backButton.changeTextColor(YELLOW)

def settingsMenu():
    
    titleText = "Game Settings"
    xPosTitle = SCREEN_WIDTH / 2
    yPosTitle = SCREEN_HEIGHT / 10
    font = pygame.font.Font(PRESS_START_2P, 70)
    titleSurface = font.render(titleText, True, YELLOW)
    titleRect = titleSurface.get_rect()
    titleRect.center = (xPosTitle, yPosTitle)
    
    running = True
    while running:
        SCREEN.blit(BACK_GROUND_JPEG, (0, 0))
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
            mouseCoord = pygame.mouse.get_pos()
            isCursorOnButtons(mouseCoord)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                isLeftButtonPressed = pygame.mouse.get_pressed()[0]
                
                if (isLeftButtonPressed):
                    if (backButton.isCursorOn(mouseCoord)):
                        running = False
            
        
        SCREEN.blit(titleSurface, titleRect)
        backButton.drawButton()
        
        pygame.display.update()