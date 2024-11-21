import pygame


GRAFFITI_TABLE_PATH = 'utils/pictures/table_pictures/GraffitiTable.png'
SEA_TABLE_PATH = 'utils/pictures/table_pictures/SeaTable.png'
DEFAULT_TABLE_PATH = 'utils/pictures/table_pictures/GraffitiTable.png'

SEA_TABLE_PNG = pygame.image.load(SEA_TABLE_PATH)
GRAFFITI_TABLE_PNG = pygame.image.load(GRAFFITI_TABLE_PATH)
DEFAULT_TABLE_PNG = pygame.image.load(DEFAULT_TABLE_PATH)

__all__ = ['SEA_TABLE_PNG', 'GRAFFITI_TABLE_PNG', 'DEFAULT_TABLE_PNG']