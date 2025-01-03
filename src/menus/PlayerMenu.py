import pygame

from utils.constants.MenuConstants import *
from utils.colors.Colors import *
from utils.fonts.Fonts import *
from utils.pictures.menu_pictures import *
from utils.pictures.buttons_pictures import *

from buttons.general_buttons.back import *
from buttons.player_settings_buttons.NameBox import *
from buttons.player_settings_buttons.PaddleSelect import *
from buttons.player_settings_buttons.PlayerSettingsBorders import *

from buttons.general_buttons.swipeLeftButton import swipeLeftButton
from buttons.general_buttons.swipeRightButton import swipeRightButton


def isCursorOnButtons(mouseCoord):
    if (backButton.isCursorOn(mouseCoord)):
        backButton.changeTextColor(CYAN)
    else:
        backButton.changeTextColor(YELLOW)

    if (swipeLeftButton.isCursorOn(mouseCoord)):
        swipeLeftButton.changeButtonImg(SWIPE_LEFT_BUTTON_BIG_PNG)
    else:
        swipeLeftButton.changeButtonImg(SWIPE_LEFT_BUTTON_PNG)
    
    if (swipeRightButton.isCursorOn(mouseCoord)):
        swipeRightButton.changeButtonImg(SWIPE_RIGHT_BUTTON__BIG_PNG)
    else:
        swipeRightButton.changeButtonImg(SWIPE_RIGHT_BUTTON_PNG)

def drawAllButtons(playerId):
    backButton.drawButton()
    swipeLeftButton.drawButton()
    swipeRightButton.drawButton()
    
    playerPaddleSelection.draw(playerId)
    playerSettingsBorders.draw()
    nameBoxes.draw(playerId)
    

def playerMenu(text, playerId):
    titleText = text
    xPosTitle = SCREEN_WIDTH / 2
    yPosTitle = SCREEN_HEIGHT / 10
    font = pygame.font.Font(PRESS_START_2P, 70)
    titleSurface = font.render(titleText, True, YELLOW)
    titleRect = titleSurface.get_rect()
    titleRect.center = (xPosTitle, yPosTitle)

    running = True


    while running:

        SCREEN.blit(BACK_GROUND_JPEG, (0, 0))
        SCREEN.blit(titleSurface, titleRect)

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
                
                if (swipeLeftButton.isCursorOn(mouseCoord)):
                    playerPaddleSelection.changeWithLeftPaddle(playerId)
                
                if (swipeRightButton.isCursorOn(mouseCoord)):
                    playerPaddleSelection.changeWithRightPaddle(playerId)

            nameBoxes.write(event, playerId)

        # Process if key is held down
        nameBoxes.processHeldKeys(playerId)

        drawAllButtons(playerId)
        
        pygame.display.update()
            

