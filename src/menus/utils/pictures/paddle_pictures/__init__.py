import pygame

PADDLE_DEFAULT_PATH = 'utils/pictures/paddle_pictures/paddle.png'
PADDLE_RED_PATH = 'utils/pictures/paddle_pictures/paddle.png'

PADDLE_DEFAULT_PNG = pygame.image.load(PADDLE_DEFAULT_PATH)
PADDLE_DEFAULT_PNG = pygame.transform.scale(PADDLE_DEFAULT_PNG, (100, 100))

PADDLE_RED_PNG = pygame.image.load(PADDLE_RED_PATH)
PADDLE_RED_PNG = pygame.transform.scale(PADDLE_RED_PNG, (100, 100))

__all__ = ['PADDLE_DEFAULT_PNG', 'PADDLE_RED_PNG']