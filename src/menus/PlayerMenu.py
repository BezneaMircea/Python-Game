from menus.Menu import Menu
from utils.TextButton import TextButton
from utils.constants.MenuConstants import *
from utils.colors.Colors import *
from utils.fonts.Fonts import *



playerOneMenuTitle = TextButton(SCREEN, SCREEN_HEIGHT / 10, SCREEN_WIDTH / 2,
                                "Player One", PRESS_START_2P, 70, YELLOW)
playerTwoMenuTitle = TextButton(SCREEN, SCREEN_HEIGHT / 10, SCREEN_WIDTH / 2,
                                "Player Two", PRESS_START_2P, 70, YELLOW)

class PlayerMenu(Menu):
    def __init__(self, rectButtons, textButtons, backGroundPicture):
        super().__init__(rectButtons, textButtons, backGroundPicture)
    



# def isCursorOnButtons(mouseCoord):
#     if (backButton.isCursorOn(mouseCoord)):
#         backButton.changeTextColor(CYAN)
#     else:
#         backButton.changeTextColor(YELLOW)

#     if (swipeLeftButton.isCursorOn(mouseCoord)):
#         swipeLeftButton.changeButtonImg(SWIPE_LEFT_BUTTON_BIG_PNG)
#     else:
#         swipeLeftButton.changeButtonImg(SWIPE_LEFT_BUTTON_PNG)
    
#     if (swipeRightButton.isCursorOn(mouseCoord)):
#         swipeRightButton.changeButtonImg(SWIPE_RIGHT_BUTTON__BIG_PNG)
#     else:
#         swipeRightButton.changeButtonImg(SWIPE_RIGHT_BUTTON_PNG)

# def drawAllButtons(playerId):
#     backButton.drawButton()
#     swipeLeftButton.drawButton()
#     swipeRightButton.drawButton()
    
#     playerPaddleSelection.draw(playerId)
#     playerSettingsBorders.draw()
#     nameBoxes.draw(playerId)
    

# def playerMenu(text, playerId):
#     titleText = text
#     xPosTitle = SCREEN_WIDTH / 2
#     yPosTitle = SCREEN_HEIGHT / 10
#     font = pygame.font.Font(PRESS_START_2P, 70)
#     titleSurface = font.render(titleText, True, YELLOW)
#     titleRect = titleSurface.get_rect()
#     titleRect.center = (xPosTitle, yPosTitle)

#     running = True


#     while running:

#         SCREEN.blit(BACK_GROUND_JPEG, (0, 0))
#         SCREEN.blit(titleSurface, titleRect)

#         for event in pygame.event.get():
            
#             if event.type == pygame.QUIT:
#                 running = False
#                 pygame.quit()
            
#             mouseCoord = pygame.mouse.get_pos()
#             isCursorOnButtons(mouseCoord)
            
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 isLeftButtonPressed = pygame.mouse.get_pressed()[0]
                
#                 if (isLeftButtonPressed):
#                     if (backButton.isCursorOn(mouseCoord)):
#                         running = False
                
#                 if (swipeLeftButton.isCursorOn(mouseCoord)):
#                     playerPaddleSelection.changeWithLeftPaddle(playerId)
                
#                 if (swipeRightButton.isCursorOn(mouseCoord)):
#                     playerPaddleSelection.changeWithRightPaddle(playerId)

#             nameBoxes.write(event, playerId)

#         # Process if key is held down
#         nameBoxes.processHeldKeys(playerId)

#         drawAllButtons(playerId)
        
        # pygame.display.update()
            

