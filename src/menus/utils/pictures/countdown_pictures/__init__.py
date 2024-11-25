import pygame

GO_PATH = 'utils/pictures/countdown_pictures/Go.png'
ONE_PATH = 'utils/pictures/countdown_pictures/One.png'
THREE_PATH = 'utils/pictures/countdown_pictures/Two.png'
TWO_PATH = 'utils/pictures/countdown_pictures/Three.png'


GO_PNG = pygame.image.load(GO_PATH)
ONE_PNG = pygame.image.load(ONE_PATH)
TWO_PNG = pygame.image.load(TWO_PATH)
THREE_PNG = pygame.image.load(THREE_PATH)

__all__ = ['GO_PNG', 'ONE_PNG', 'TWO_PNG', 'THREE_PNG']