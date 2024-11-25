from utils.pictures.table_pictures import *
from utils.constants.MenuConstants import *
from utils.RectButton import RectButton
from game.GameSettup import currentGameSettings

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

def changeWithTableOnLeft():
    global imageListLeft
    global imageListRight
    global currentImage
    
    if not imageListLeft:
        return
    
    newImage = imageListLeft.pop(0)
    imageListRight.insert(0, currentImage)
    imageListLeft.append(imageListRight.pop(len(imageListRight) - 1))
    currentImage = newImage
    
    mapSelect.changeButtonImg(currentImage[1])
    mapLeft.changeButtonImg(imageListLeft[0][0])
    mapRight.changeButtonImg(imageListRight[0][0])
    
    currentGameSettings.changeTable(currentImage[2])
     
def changeWithTableOnRight():
    global imageListLeft
    global imageListRight
    global currentImage
    
    if not imageListRight:
        return

    newImage = imageListRight.pop(0)
    imageListLeft.insert(0, currentImage)
    imageListRight.append(imageListLeft.pop(len(imageListLeft) - 1))
    currentImage = newImage

    mapSelect.changeButtonImg(currentImage[1])
    mapLeft.changeButtonImg(imageListLeft[0][0])
    mapRight.changeButtonImg(imageListRight[0][0])
    
    currentGameSettings.changeTable(currentImage[2])


__all__ = ['mapSelect', 'mapLeft', 'mapRight',
           'changeWithTableOnRight', 'changeWithTableOnLeft']