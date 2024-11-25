import pygame

PUCK_DEFAULT_PATH = 'utils/pictures/puck_pictures/puck.png'
PUCK_RED_PATH = 'utils/pictures/puck_pictures/puck.png'

PUCK_DEFAULT_PNG = pygame.image.load(PUCK_DEFAULT_PATH)
PUCK_DEFAULT_PNG = pygame.transform.scale(PUCK_DEFAULT_PNG, (70, 70))

PUCK_RED_PNG = pygame.image.load(PUCK_DEFAULT_PATH)
PUCK_RED_PNG = pygame.transform.scale(PUCK_RED_PNG, (70, 70))

__all__ = ['PUCK_DEFAULT_PNG', 'PUCK_RED_PNG']