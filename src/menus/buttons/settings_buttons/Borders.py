import pygame
import numpy as np
from utils.pictures.table_pictures import *
from utils.constants.MenuConstants import *
from menus.buttons.settings_buttons.MapSelect import (
    IMAGE_SIZE,
    IMAGE_SIZE_SMALL,
    
    SMALL_PICTURE_XPOS,
    SMALL_PICTURE_YPOS_LEFT,
    SMALL_PICTURE_YPOS_RIGHT,
    
    CENTER_PICTURE_XPOS,
    CENTER_PICTURE_YPOS
)    
from utils.RectButton import RectButton

BORDER_EXTRA_LENGTH = (2, 5)


BORDER_SIZE_BIG = tuple(np.add(IMAGE_SIZE, BORDER_EXTRA_LENGTH))
BORDER_SIZE_SMALL = tuple(np.add(IMAGE_SIZE_SMALL, BORDER_EXTRA_LENGTH))


imageBorderMedium =  pygame.transform.scale(BORDER_PNG, BORDER_SIZE_BIG)
imageBorderSmall = pygame.transform.scale(BORDER_PNG, BORDER_SIZE_SMALL)


borderLeft = RectButton(SCREEN, SMALL_PICTURE_XPOS, SMALL_PICTURE_YPOS_LEFT, imageBorderSmall)
borderCentre = RectButton(SCREEN, CENTER_PICTURE_XPOS, CENTER_PICTURE_YPOS, imageBorderMedium)
borderRight = RectButton(SCREEN, SMALL_PICTURE_XPOS, SMALL_PICTURE_YPOS_RIGHT, imageBorderSmall)

class MapSelectionBorders():
    def __init__(self, borderLeft, borderCentre, borderRight):
        self.borderLeft = borderLeft
        self.borderCentre = borderCentre
        self.borderRight = borderRight
        
    def drawButton(self):
        self.borderRight.drawButton()
        self.borderCentre.drawButton()
        self.borderLeft.drawButton()
    
    def interactWithCursor(self, mouseCoord):
        pass

    def performAction(self, mouseCoord, pressed):
        pass


mapSelectionBorders = MapSelectionBorders(borderLeft, borderCentre, borderRight)

__all__ = ['mapSelectionBorders']