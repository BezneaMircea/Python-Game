import pygame

from menus.Menu import Menu

from utils.constants.MenuConstants import *
from utils.colors.Colors import *
from utils.fonts.Fonts import *
from utils.pictures.menu_pictures import *
from utils.pictures.buttons_pictures import *

from menus.buttons.general_buttons.back import *
# from menus.buttons.settings_buttons.MapSelect import *

# from menus.buttons.general_buttons.swipeLeftButton import swipeLeftButton
# from menus.buttons.general_buttons.swipeRightButton import swipeRightButton
# from menus.buttons.settings_buttons.Borders import *
# from menus.buttons.settings_buttons.control_bars.TimeControl import timeControl
# from menus.buttons.settings_buttons.control_bars.VolumeControl import volumeControl

from game.GameSetup import *

titleText = "Game Settings"
xPosTitle = SCREEN_WIDTH / 2
yPosTitle = SCREEN_HEIGHT / 10
font = pygame.font.Font(PRESS_START_2P, 70)
titleSurface = font.render(titleText, True, YELLOW)
titleRect = titleSurface.get_rect()
titleRect.center = (xPosTitle, yPosTitle)

class SettingsMenu(Menu):
    def __init__(self, screen, rectButtons, textButtons):
        super().__init__(rectButtons, textButtons)
        self.screen = screen

    def settingsMenuLoop(self):

        running = True

        # isPressedTime = False
        # isPressedVolume = False
        while running:
            
            SCREEN.blit(BACK_GROUND_JPEG, (0, 0))
            SCREEN.blit(titleSurface, titleRect)
                
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                
                mouseCoord = pygame.mouse.get_pos()
                super().buttonsInteractions(mouseCoord)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    isLeftButtonPressed = pygame.mouse.get_pressed()[0]
                    
                    if isLeftButtonPressed:
                        self.performButtonActions(mouseCoord)
                        if (backButton.isCursorOn(mouseCoord)):
                            running = False
                            
                        # if (swipeLeftButton.isCursorOn(mouseCoord)):
                        #     mapSelection.changeWithTableOnLeft()

                        # if (swipeRightButton.isCursorOn(mouseCoord)):
                        #     mapSelection.changeWithTableOnRight()
            
            # mouseCoord = pygame.mouse.get_pos()
            # pressedMouse = pygame.mouse.get_pressed()
            
            
            # if (timeControl.barButton.isCursorOn(mouseCoord) and pressedMouse[0]
            #     and not isPressedVolume):
            #     isPressedTime = True
            
            # if (volumeControl.barButton.isCursorOn(mouseCoord) and pressedMouse[0]
            #     and not isPressedTime):
            #     isPressedVolume = True
                
            
            # if not pressedMouse[0]:
            #     isPressedTime = False
            #     isPressedVolume = False

            # if (isPressedTime):
            #     timeControl.move(mouseCoord)
            
            # if (isPressedVolume):
            #     volumeControl.move(mouseCoord)
            
            super().drawAllButtons()
            
            pygame.display.update()