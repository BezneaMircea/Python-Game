from utils.pictures.table_pictures import *
from utils.constants.MenuConstants import *
from utils.RectButton import RectButton
from game.GameSetup import currentGameSettings

import pygame

IMAGE_SIZE = (250, 150)
IMAGE_SIZE_SMALL = (150, 100)

SMALL_PICTURE_XPOS = SCREEN_HEIGHT - 3 * SCREEN_HEIGHT / 10 + 40
SMALL_PICTURE_YPOS_LEFT = SCREEN_WIDTH / 2 - 250
SMALL_PICTURE_YPOS_RIGHT = SCREEN_WIDTH / 2 + 250

CENTER_PICTURE_XPOS = SCREEN_HEIGHT - 3 * SCREEN_HEIGHT / 10
CENTER_PICTURE_YPOS = SCREEN_WIDTH / 2

# Medium size picture for the selected picture in the gameSettings
imageDefaultMedium =  pygame.transform.scale(DEFAULT_TABLE_PNG, IMAGE_SIZE)
imageSeaMedium = pygame.transform.scale(SEA_TABLE_PNG, IMAGE_SIZE)
imageGraffitiMedium = pygame.transform.scale(GRAFFITI_TABLE_PNG, IMAGE_SIZE)

# Small size picture for the pictures that are not curently selected in gameSettings
imageDefaultSmall = pygame.transform.scale(DEFAULT_TABLE_PNG, IMAGE_SIZE_SMALL)
imageSeaSmall = pygame.transform.scale(SEA_TABLE_PNG, IMAGE_SIZE_SMALL)
imageGraffitiSmall = pygame.transform.scale(GRAFFITI_TABLE_PNG, IMAGE_SIZE_SMALL)


mapSelect = RectButton(SCREEN, CENTER_PICTURE_XPOS, CENTER_PICTURE_YPOS, imageDefaultMedium)
mapLeft = RectButton(SCREEN, SMALL_PICTURE_XPOS, SMALL_PICTURE_YPOS_LEFT, imageGraffitiSmall)
mapRight = RectButton(SCREEN, SMALL_PICTURE_XPOS, SMALL_PICTURE_YPOS_RIGHT, imageSeaSmall)


#Add more maps to left or right
imageListLeft = [(imageGraffitiSmall, imageGraffitiMedium, GRAFFITI_TABLE_PNG)]
imageListRight = [(imageSeaSmall, imageSeaMedium, SEA_TABLE_PNG)]

currentImage = (imageDefaultSmall, imageDefaultMedium , DEFAULT_TABLE_PNG)
class MapSelect:
    def __init__(self, imageListLeft, imageListRight, curImg,
                 mapSelect, mapLeft, mapRight):
        self.imageListLeft = imageListLeft
        self.imageListRight = imageListRight
        self.curImg = curImg
        self.mapSelect = mapSelect
        self.mapLeft = mapLeft
        self.mapRight = mapRight
    
    def changeWithTableOnLeft(self):
        if not self.imageListLeft:
            return
        
        newImage = self.imageListLeft.pop(0)
        self.imageListRight.insert(0, self.curImg)
        self.imageListLeft.append(self.imageListRight.pop(len(self.imageListRight) - 1))
        self.curImg = newImage
        
        self.mapSelect.changeButtonImg(self.curImg[1])
        self.mapLeft.changeButtonImg(self.imageListLeft[0][0])
        self.mapRight.changeButtonImg(self.imageListRight[0][0])
        
        currentGameSettings.changeTable(self.curImg[2])
        
    def changeWithTableOnRight(self):
        if not self.imageListRight:
            return

        newImage = self.imageListRight.pop(0)
        self.imageListLeft.insert(0, self.curImg)
        self.imageListRight.append(self.imageListLeft.pop(len(self.imageListLeft) - 1))
        self.curImg = newImage

        self.mapSelect.changeButtonImg(self.curImg[1])
        self.mapLeft.changeButtonImg(self.imageListLeft[0][0])
        self.mapRight.changeButtonImg(self.imageListRight[0][0])
        
        currentGameSettings.changeTable(self.curImg[2])
        
    def draw(self):
        self.mapSelect.drawButton()
        self.mapLeft.drawButton()
        self.mapRight.drawButton()

mapSelection = MapSelect(imageListLeft, imageListRight, currentImage,
                         mapSelect, mapLeft, mapRight)


__all__ = ['mapSelection']