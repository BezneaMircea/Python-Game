import pygame

GATE_PATH = 'utils/pictures/gate_picture/gate.png'

GATE_PNG = pygame.image.load(GATE_PATH)
GATE_PNG = pygame.transform.scale(GATE_PNG, (14, 210))

__all__ = ['GATE_PNG']