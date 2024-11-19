import pygame
from utils import *

# Can be changed depending on what resolution we want
pygame.init()


backgroundImg = pygame.image.load(BACKGROUND_PATH)


# Upper Text

titleText = "Air Hockey"
xPosTitle = SCREEN_WIDTH / 2
yPosTitle = SCREEN_HEIGHT / 10
font = pygame.font.Font(PRESS_START_2P, 70)
titleSurface = font.render(titleText, True, TITLE_COLOR)
titleRect = titleSurface.get_rect()
titleRect.center = (xPosTitle, yPosTitle)

# The Quit Button
textQuit = "Quit"
xPosQuit = SCREEN_HEIGHT - (SCREEN_HEIGHT) / 10
yPosQuit = (SCREEN_WIDTH) / 2
fontQuit = pygame.font.Font(PRESS_START_2P, 36)
colorQuit = TEXT_COLOR_NOT_TOUCHED

# The Setting Button
textSettings = "Settings"
xPosSettings = xPosQuit - DISTANCE_BEETWEEN_BUTTONS
yPosSettings = yPosQuit
fontSettings = pygame.font.Font(PRESS_START_2P, 20)
colorSetting = TEXT_COLOR_NOT_TOUCHED

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:

    buttonQuit = RectButton(screen=screen, xPos=xPosQuit, yPos=yPosQuit, path=BUTTON_PATH)
    buttonQuit.addTextToButton(textQuit, fontQuit, colorQuit)
    
    buttonSettings = RectButton(screen=screen, xPos=xPosSettings, yPos=yPosSettings, path=BUTTON_PATH)
    buttonSettings.addTextToButton(textSettings, fontSettings, colorSetting)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
    
        if (buttonQuit.isCursorOn(pygame.mouse.get_pos())):
            colorQuit = TEXT_COLOR_TOUCHED
        else:
            colorQuit = TEXT_COLOR_NOT_TOUCHED
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if(buttonQuit.isCursorOn(pygame.mouse.get_pos())):
                    running = False
    
    screen.blit(backgroundImg, (0, 0))
    screen.blit(titleSurface, titleRect)
    
    buttonQuit.drawButton()
    buttonSettings.drawButton()

    pygame.display.flip()
        
             
pygame.quit()