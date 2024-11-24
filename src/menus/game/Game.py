import pygame
from game.GameSettup import *
from utils.constants.MenuConstants import *



def game():
    running = True
    while running:
        SCREEN.blit(currentGameSettings.currentTableImg, (0, 0))
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                running = False
                #pygame.quit()
                
        pygame.display.update()