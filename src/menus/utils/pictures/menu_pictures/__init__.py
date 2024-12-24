import pygame

BACK_GROUND_JPEG_PATH = 'utils/pictures/menu_pictures/BackGround.jpeg' 
BARA_PNG_PATH = 'utils/pictures/menu_pictures/Bara.png'
SCROLL_BUTTON_PATH = 'utils/pictures/menu_pictures/ScrollButton.png'


BACK_GROUND_JPEG = pygame.image.load(BACK_GROUND_JPEG_PATH)
BARA_PNG = pygame.image.load(BARA_PNG_PATH)
SCROLL_BUTTON_PNG = pygame.image.load(SCROLL_BUTTON_PATH)


__all__ = ['BACK_GROUND_JPEG', 'BARA_PNG', 'SCROLL_BUTTON_PNG']