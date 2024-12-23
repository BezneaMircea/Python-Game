import pygame

BLUE_PADDLE_PNG_PATH = 'utils/pictures/paddle_pictures/Blue_Paddle.png'
PURPLE_PADDLE_PNG_PATH = 'utils/pictures/paddle_pictures/Purple_Paddle.png'
ORANGE_PADDLE_PNG_PATH = 'utils/pictures/paddle_pictures/Orange_Paddle.png'
DEFAULT_PADDLE_PNG_PATH = 'utils/pictures/paddle_pictures/Orange_Paddle.png'

BLUE_PADDLE_PNG = pygame.image.load(BLUE_PADDLE_PNG_PATH)
PURPLE_PADDLE_PNG = pygame.image.load(PURPLE_PADDLE_PNG_PATH)
ORANGE_PADDLE_PNG = pygame.image.load(ORANGE_PADDLE_PNG_PATH)
DEFAULT_PADDLE_PNG = pygame.image.load(DEFAULT_PADDLE_PNG_PATH)


__all__ = ['BLUE_PADDLE_PNG', 'PURPLE_PADDLE_PNG',
           'ORANGE_PADDLE_PNG', 'DEFAULT_PADDLE_PNG']
