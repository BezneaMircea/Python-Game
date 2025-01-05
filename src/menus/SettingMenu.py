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
from menus.buttons.settings_buttons.control_bars.TimeControl import timeControl
from menus.buttons.settings_buttons.control_bars.VolumeControl import volumeControl

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
        while running:
            
            SCREEN.blit(BACK_GROUND_JPEG, (0, 0))
            SCREEN.blit(titleSurface, titleRect)
                
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                
                mouseCoord = pygame.mouse.get_pos()
                super().buttonsInteractions(mouseCoord)
                
                pressed = pygame.mouse.get_pressed()
                self.performButtonActions(mouseCoord, pressed)
                if (backButton.isCursorOn(mouseCoord)):
                    running = False

            
            super().drawAllButtons()
            
            pygame.display.update()