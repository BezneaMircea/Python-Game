import pygame

from menus.Menu import Menu


# Before refactoring 
from utils.pictures.menu_pictures import *
from utils.constants.MenuConstants import *

from utils.colors.Colors import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.music.Music import *
from utils.TextButton import TextButton


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


startMenuText = TextButton(SCREEN, SCREEN_HEIGHT / 10, SCREEN_WIDTH / 2, 
                           "Air Hockey", PRESS_START_2P, 70, YELLOW)

class StartMenu(Menu):
    def __init__(self, rectButtons, textButtons, backGroundPicture):
        super().__init__(rectButtons, textButtons, backGroundPicture)
    

    # def startMenuLoop(self):
        #There are some problems here
        #song Must enter a loop.
        #playSong(APO_SOLO_PATH_MP3)
        # while self.running:

        #     SCREEN.blit(BACK_GROUND_JPEG, (0, 0))
        #     SCREEN.blit(titleSurface, titleRect)    
            
        #     for event in pygame.event.get():        
                
        #         if event.type == pygame.QUIT:
        #             self.running = False
                
        #         mouseCoord = pygame.mouse.get_pos()
        #         super().buttonsInteractions(mouseCoord)

        #         pressed = pygame.mouse.get_pressed()
        #         self.performButtonActions(mouseCoord, pressed)

        #                 # if (settingsButton.isCursorOn(mouseCoord)):
        #                 #     pass 
        #                 #     # settingsMenu()
                    

        #                 # if (playerOneButton.isCursorOn(mouseCoord)):
        #                 #     pass 
        #                 #     # playerMenu("Player One", 1)
                        
        #                 # if (playerTwoButton.isCursorOn(mouseCoord)):
        #                 #     pass 
        #                 #     # playerMenu("Player Two", 2)

        #     super().drawAllButtons()
            

        #     pygame.display.update()  
                
        # pygame.quit()

   