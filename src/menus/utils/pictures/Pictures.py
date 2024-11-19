import pygame

BACK_GROUND_JPEG_PATH = 'utils/pictures/BackGround.jpeg'
BUTTON_PNG_PATH = 'utils/pictures/Button.png'

BACK_GROUND_JPEG = pygame.image.load(BACK_GROUND_JPEG_PATH)
BUTTON_PNG = pygame.image.load(BUTTON_PNG_PATH)

__all__ = ['BACK_GROUND_JPEG', 'BUTTON_PNG']