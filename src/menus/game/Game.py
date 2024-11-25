import pygame
from game.GameSettup import *
from utils.constants.MenuConstants import *


playerOne = currentGameSettings.playerOne
playerTwo = currentGameSettings.playerTwo
puck = currentGameSettings.puck

def game():
    running = True

    while running:
        SCREEN.blit(currentGameSettings.currentTableImg, (0, 0))
    
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                running = False
                playerOne.paddle.resetPosition()
                playerTwo.paddle.resetPosition()
                puck.resetPosition()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    playerOne.paddle.resetPosition()
                    playerTwo.paddle.resetPosition()
                    puck.resetPosition()
                # pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[playerOne.controls[0]]:
            playerOne.paddle.moveLeft()
        if keys[playerOne.controls[1]]:
            playerOne.paddle.moveRight()
        if keys[playerOne.controls[2]]:
            playerOne.paddle.moveUp()
        if keys[playerOne.controls[3]]:
            playerOne.paddle.moveDown()

        if keys[playerTwo.controls[0]]:
            playerTwo.paddle.moveLeft()
        if keys[playerTwo.controls[1]]:
            playerTwo.paddle.moveRight()
        if keys[playerTwo.controls[2]]:
            playerTwo.paddle.moveUp()
        if keys[playerTwo.controls[3]]:
            playerTwo.paddle.moveDown()
    
        playerOne.paddle.draw()
        playerTwo.paddle.draw()
        puck.draw()

        pygame.display.update()