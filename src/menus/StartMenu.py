import pygame

from menus.Menu import Menu


# Before refactoring 
from utils.pictures.menu_pictures import *
from utils.constants.MenuConstants import *

from utils.colors.Colors import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.music.Music import *


from menus.buttons.start_buttons.Quit import *
# from menus.buttons.start_buttons.Setting import *
# from menus.buttons.start_buttons.Play import *
# from menus.buttons.start_buttons.PlayerOne import *
# from menus.buttons.start_buttons.PlayerTwo import *


# from menus.SettingMenu import settingsMenu
# from menus.PlayerMenu import playerMenu
# from game.GameSetup import currentGameSettings
# from game.Game import Game


# Can be changed depending on what resolution we want
# Upper Text

titleText = "Air Hockey"
xPosTitle = SCREEN_WIDTH / 2
yPosTitle = SCREEN_HEIGHT / 10
font = pygame.font.Font(PRESS_START_2P, 70)
titleSurface = font.render(titleText, True, YELLOW)
titleRect = titleSurface.get_rect()
titleRect.center = (xPosTitle, yPosTitle)

class StartMenu(Menu):
    def __init__(self, screen, rectButtons, textButtons):
        super().__init__(rectButtons, textButtons)
        self.screen = screen
    
        
    def startMenuLoop(self):
        #There are some problems here
        #song Must enter a loop.
        #playSong(APO_SOLO_PATH_MP3)
        while self.running:

            SCREEN.blit(BACK_GROUND_JPEG, (0, 0))
            SCREEN.blit(titleSurface, titleRect)    
            
            for event in pygame.event.get():        
                
                if event.type == pygame.QUIT:
                    self.running = False
                
                mouseCoord = pygame.mouse.get_pos()
                super().buttonsInteractions(mouseCoord)

                pressed = pygame.mouse.get_pressed()
                self.performButtonActions(mouseCoord, pressed)

                        # if (settingsButton.isCursorOn(mouseCoord)):
                        #     pass 
                        #     # settingsMenu()
                    

                        # if (playerOneButton.isCursorOn(mouseCoord)):
                        #     pass 
                        #     # playerMenu("Player One", 1)
                        
                        # if (playerTwoButton.isCursorOn(mouseCoord)):
                        #     pass 
                        #     # playerMenu("Player Two", 2)

            super().drawAllButtons()
            

            pygame.display.update()  
                
        pygame.quit()

   