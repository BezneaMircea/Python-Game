import pygame
from utils import *
from utils.pictures.Pictures import BACK_GROUND_JPEG
from utils.pictures.Pictures import BUTTON_PNG
from utils.colors.Colors import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.RectButton import RectButton

# Can be changed depending on what resolution we want
pygame.init()


# Upper Text

titleText = "Air Hockey"
xPosTitle = SCREEN_WIDTH / 2
yPosTitle = SCREEN_HEIGHT / 10
font = pygame.font.Font(PRESS_START_2P, 70)
titleSurface = font.render(titleText, True, YELLOW)
titleRect = titleSurface.get_rect()
titleRect.center = (xPosTitle, yPosTitle)

# The Quit Button
textQuit = "Quit"
xPosQuit = SCREEN_HEIGHT - (SCREEN_HEIGHT) / 10
yPosQuit = (SCREEN_WIDTH) / 2
fontQuit = pygame.font.Font(PRESS_START_2P, 36)
colorQuit = YELLOW

# The Setting Button
textSettings = "Settings"
xPosSettings = xPosQuit - DISTANCE_BEETWEEN_BUTTONS
yPosSettings = yPosQuit
fontSettings = pygame.font.Font(PRESS_START_2P, 20)
colorSetting = YELLOW

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:

    buttonQuit = RectButton(screen=screen, xPos=xPosQuit, yPos=yPosQuit, image=BUTTON_PNG)
    buttonQuit.addTextToButton(textQuit, fontQuit, colorQuit)
    
    buttonSettings = RectButton(screen=screen, xPos=xPosSettings, yPos=yPosSettings, image=BUTTON_PNG)
    buttonSettings.addTextToButton(textSettings, fontSettings, colorSetting)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
    
        if (buttonQuit.isCursorOn(pygame.mouse.get_pos())):
            colorQuit = RED
        else:
            colorQuit = YELLOW
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if(buttonQuit.isCursorOn(pygame.mouse.get_pos())):
                    running = False
    
    screen.blit(BACK_GROUND_JPEG, (0, 0))
    screen.blit(titleSurface, titleRect)
    
    buttonQuit.drawButton()
    buttonSettings.drawButton()

    pygame.display.flip()
        
             
pygame.quit()