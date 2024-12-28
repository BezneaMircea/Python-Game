import pygame

from utils.constants.MenuConstants import *
from utils.colors.Colors import *
from utils.fonts.Fonts import *
from utils.pictures.menu_pictures import *
from utils.pictures.buttons_pictures import *

from buttons.general_buttons.back import *
from buttons.settings_buttons.MapSelect import *

from buttons.general_buttons.swipeLeftButton import swipeLeftButton
from buttons.general_buttons.swipeRightButton import swipeRightButton
from buttons.settings_buttons.Borders import *
from buttons.settings_buttons.control_bars.TimeControl import timeControl
from buttons.settings_buttons.control_bars.VolumeControl import volumeControl

from game.GameSetup import *

titleText = "Game Settings"
xPosTitle = SCREEN_WIDTH / 2
yPosTitle = SCREEN_HEIGHT / 10
font = pygame.font.Font(PRESS_START_2P, 70)
titleSurface = font.render(titleText, True, YELLOW)
titleRect = titleSurface.get_rect()
titleRect.center = (xPosTitle, yPosTitle)


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

def drawAllButtons():
    backButton.drawButton()
    swipeLeftButton.drawButton()
    swipeRightButton.drawButton()
    mapSelection.draw()
    mapSelectionBorders.draw()
    timeControl.draw()
    volumeControl.draw()
    
def settingsMenu():
    
    running = True
    
    isPressedTime = False
    isPressedVolume = False
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
                        mapSelection.changeWithTableOnLeft()

                    if (swipeRightButton.isCursorOn(mouseCoord)):
                        mapSelection.changeWithTableOnRight()
        
        mouseCoord = pygame.mouse.get_pos()
        pressedMouse = pygame.mouse.get_pressed()
        
        
        if (timeControl.barButton.isCursorOn(mouseCoord) and pressedMouse[0]):
            isPressedTime = True
        
        if (volumeControl.barButton.isCursorOn(mouseCoord) and pressedMouse[0]):
            isPressedVolume = True
            
        
        if not pressedMouse[0]:
            isPressedTime = False
            isPressedVolume = False

        if (isPressedTime):
            timeControl.move(mouseCoord)
        
        if (isPressedVolume):
            volumeControl.move(mouseCoord)
        
        drawAllButtons()
        
        pygame.display.update()