import pygame

BACK_GROUND_JPEG_PATH = 'utils/pictures/BackGround.jpeg'
BUTTON_PNG_PATH = 'utils/pictures/Button.png'
GRAFFITI_TABLE_PATH = 'utils/pictures/GraffitiTable.png'
SEA_TABLE_PATH = 'utils/pictures/SeaTable.png'
DEFAULT_TABLE_PATH = 'utils/pictures/GraffitiTable.png'

BACK_GROUND_JPEG = pygame.image.load(BACK_GROUND_JPEG_PATH)
BUTTON_PNG = pygame.image.load(BUTTON_PNG_PATH)
SEA_TABLE_PNG = pygame.image.load(SEA_TABLE_PATH)
GRAFFITI_TABLE_PNG = pygame.image.load(GRAFFITI_TABLE_PATH)
DEFAULT_TABLE_PNG = pygame.image.load(DEFAULT_TABLE_PATH)

__all__ = ['BACK_GROUND_JPEG', 'BUTTON_PNG', 'GRAFFITI_TABLE_PNG',
           'SEA_TABLE_PNG', 'DEFAULT_TABLE_PNG']