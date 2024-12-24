import pygame
from utils.constants.MenuConstants import *
from utils.pictures.countdown_pictures import COUNTDOWN

class Game:
    def __init__(self, currentGameSettings):
        self.tableImg = currentGameSettings.currentTableImg
        self.playerOne = currentGameSettings.playerOne
        self.playerTwo = currentGameSettings.playerTwo
        self.puck = currentGameSettings.puck
        
    def beginningTimer(self):
        clock = pygame.time.Clock()

        currentImageIndex = 0
        lastSwitchTime = pygame.time.get_ticks()
        
        running = True
        while running:
            SCREEN.blit(self.tableImg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Get the current time
            currentTime = pygame.time.get_ticks()

            # Check if 1 second has passed since the last switch
            if currentTime - lastSwitchTime >= 1000:
                currentImageIndex += 1
                if currentImageIndex >= len(COUNTDOWN):
                    currentImageIndex = 0
                lastSwitchTime = currentTime

            SCREEN.blit(COUNTDOWN[currentImageIndex], (0, 0))

            pygame.display.flip()

            
            if currentImageIndex == len(COUNTDOWN) - 1:
                pygame.time.wait(1000)
                running = False
                
            
    def start(self):
        # FOR GHENI: Just comment this function if it annoys you:
        self.beginningTimer()
        #
        running = True
        while running:
            SCREEN.blit(self.tableImg, (0, 0))
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    running = False
                    self.playerOne.paddle.resetPosition()
                    self.playerTwo.paddle.resetPosition()
                    self.puck.resetPosition()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        self.playerOne.paddle.resetPosition()
                        self.playerTwo.paddle.resetPosition()
                        self.puck.resetPosition()
                    # pygame.quit()

            keys = pygame.key.get_pressed()

            if keys[self.playerOne.controls[0]]:
                self.playerOne.paddle.moveLeft()
            if keys[self.playerOne.controls[1]]:
                self.playerOne.paddle.moveRight()
            if keys[self.playerOne.controls[2]]:
                self.playerOne.paddle.moveUp()
            if keys[self.playerOne.controls[3]]:
                self.playerOne.paddle.moveDown()

            if keys[self.playerTwo.controls[0]]:
                self.playerTwo.paddle.moveLeft()
            if keys[self.playerTwo.controls[1]]:
                self.playerTwo.paddle.moveRight()
            if keys[self.playerTwo.controls[2]]:
                self.playerTwo.paddle.moveUp()
            if keys[self.playerTwo.controls[3]]:
                self.playerTwo.paddle.moveDown()
            
            self.puck.move()
            self.puck.collision(self.playerOne.paddle)
            self.puck.collision(self.playerTwo.paddle)
            

            self.playerOne.paddle.draw()
            self.playerTwo.paddle.draw()
            self.puck.draw()

            pygame.display.update()

__all__ = ['Game']