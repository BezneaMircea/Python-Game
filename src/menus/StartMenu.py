import pygame

from utils.constants.MenuConstants import *
from utils.pictures.Pictures import *
from utils.colors.Colors import *
from utils.fonts.Fonts import PRESS_START_2P

from buttons.start_buttons.Quit import *
from buttons.start_buttons.Setting import *
from buttons.start_buttons.Play import *
from buttons.start_buttons.PlayerOne import *
from buttons.start_buttons.PlayerTwo import *

from SettingMenu import settingsMenu
from PlayerMenu import playerMenu
from game.Game import game



# Can be changed depending on what resolution we want
# Upper Text

titleText = "Air Hockey"
xPosTitle = SCREEN_WIDTH / 2
yPosTitle = SCREEN_HEIGHT / 10
font = pygame.font.Font(PRESS_START_2P, 70)
titleSurface = font.render(titleText, True, YELLOW)
titleRect = titleSurface.get_rect()
titleRect.center = (xPosTitle, yPosTitle)


def isCursorOnButtons(mouseCoord):
    if (quitButton.isCursorOn(mouseCoord)):
        quitButton.changeTextColor(RED)
    else:
        quitButton.changeTextColor(YELLOW)
            
    if (settingsButton.isCursorOn(mouseCoord)):
        settingsButton.changeTextColor(CYAN)
    else:
        settingsButton.changeTextColor(YELLOW)
    
    if (playButton.isCursorOn(mouseCoord)):
        playButton.changeTextColor(LIME_GREEN)
    else:
        playButton.changeTextColor(YELLOW)

    if (playerOneButton.isCursorOn(mouseCoord)):
        playerOneButton.changeTextColor(CYAN)
    else:
        playerOneButton.changeTextColor(YELLOW)
    
    if (playerTwoButton.isCursorOn(mouseCoord)):
        playerTwoButton.changeTextColor(CYAN)
    else:
        playerTwoButton.changeTextColor(YELLOW)


def drawAllButtons():
    quitButton.drawButton()
    settingsButton.drawButton()
    playButton.drawButton()
    playerOneButton.drawButton()
    playerTwoButton.drawButton()

running = True

while running:
    
    SCREEN.blit(BACK_GROUND_JPEG, (0, 0))
    SCREEN.blit(titleSurface, titleRect)
    
    for event in pygame.event.get():        
        
        if event.type == pygame.QUIT:
            running = False
        
        mouseCoord = pygame.mouse.get_pos()
        isCursorOnButtons(mouseCoord)

        if event.type == pygame.MOUSEBUTTONDOWN:
            isLeftButtonPressed = pygame.mouse.get_pressed()[0]
            
            if isLeftButtonPressed:
                if (quitButton.isCursorOn(mouseCoord)):
                    running = False

                if (settingsButton.isCursorOn(mouseCoord)):
                    settingsMenu()
 
            
                if (playButton.isCursorOn(mouseCoord)):
                    game()

                
                if (playerOneButton.isCursorOn(mouseCoord)):
                    playerMenu("Player One")
                
                if (playerTwoButton.isCursorOn(mouseCoord)):
                    playerMenu("Player Two")

    
    

    drawAllButtons()

    pygame.display.update()
        
             
pygame.quit()