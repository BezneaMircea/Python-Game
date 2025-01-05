import pygame

BUTTON_PNG_PATH = 'utils/pictures/buttons_pictures/Button.png'
SWIPE_BUTTON_PNG_PATH = 'utils/pictures/buttons_pictures/SwipeButtonTwo.png'
BARA_PNG_PATH = 'utils/pictures/buttons_pictures/Bara.png'
SCROLL_BUTTON_PATH = 'utils/pictures/buttons_pictures/ScrollButton.png'
NAME_BOX_PATH = 'utils/pictures/buttons_pictures/NameBox.png'



BARA_PNG = pygame.image.load(BARA_PNG_PATH)
SCROLL_BUTTON_PNG = pygame.image.load(SCROLL_BUTTON_PATH)

BUTTON_PNG = pygame.image.load(BUTTON_PNG_PATH)
NAMEBOX_PNG = pygame.image.load(NAME_BOX_PATH)

SWIPE_BUTTON_PNG = pygame.image.load(SWIPE_BUTTON_PNG_PATH)
SWIPE_BUTTON_PNG = pygame.transform.scale(SWIPE_BUTTON_PNG, (50, 70))

SWIPE_LEFT_BUTTON_PNG = pygame.transform.rotate(SWIPE_BUTTON_PNG, 180)
SWIPE_RIGHT_BUTTON_PNG = SWIPE_BUTTON_PNG

SWIPE_LEFT_BUTTON_BIG_PNG = pygame.transform.scale(SWIPE_LEFT_BUTTON_PNG, (70, 90))
SWIPE_RIGHT_BUTTON__BIG_PNG = pygame.transform.scale(SWIPE_RIGHT_BUTTON_PNG, (70, 90))

__all__ = ['BUTTON_PNG', 'SWIPE_LEFT_BUTTON_PNG', 'SWIPE_RIGHT_BUTTON_PNG',
           'SWIPE_LEFT_BUTTON_BIG_PNG', 'SWIPE_RIGHT_BUTTON__BIG_PNG',
           'BARA_PNG', 'SCROLL_BUTTON_PNG', 'NAMEBOX_PNG']