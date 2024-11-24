import pygame

BUTTON_PNG_PATH = 'utils/pictures/buttons_pictures/Button.png'
SWIPE_BUTTON_PNG_PATH = 'utils/pictures/buttons_pictures/SwipeButtonTwo.png'

BUTTON_PNG = pygame.image.load(BUTTON_PNG_PATH)
SWIPE_BUTTON_PNG = pygame.image.load(SWIPE_BUTTON_PNG_PATH)
SWIPE_BUTTON_PNG = pygame.transform.scale(SWIPE_BUTTON_PNG, (50, 70))

SWIPE_LEFT_BUTTON_PNG = pygame.transform.rotate(SWIPE_BUTTON_PNG, 180)
SWIPE_RIGHT_BUTTON_PNG = SWIPE_BUTTON_PNG

SWIPE_LEFT_BUTTON_BIG_PNG = pygame.transform.scale(SWIPE_LEFT_BUTTON_PNG, (70, 90))
SWIPE_RIGHT_BUTTON__BIG_PNG = pygame.transform.scale(SWIPE_RIGHT_BUTTON_PNG, (70, 90))

__all__ = ['BUTTON_PNG', 'SWIPE_LEFT_BUTTON_PNG', 'SWIPE_RIGHT_BUTTON_PNG',
           'SWIPE_LEFT_BUTTON_BIG_PNG', 'SWIPE_RIGHT_BUTTON__BIG_PNG']