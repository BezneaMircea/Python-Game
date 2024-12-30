from game.Paddle import *
import pygame


class Player:
    def __init__(self, name, paddle, controls):
        self.name = name
        self.score = 0
        self.paddle = paddle
        self.controls = controls
    
    def changePlayerPaddle(self, image):
        self.paddle.changeImg(image)
        
playerOne = Player('Player One', paddleOne, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s))
playerTwo = Player('Player Two', paddleTwo, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN))

__all__ = ['playerOne', 'playerTwo']