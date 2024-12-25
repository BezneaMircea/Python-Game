from utils.pictures.table_pictures import *
from utils.constants.MenuConstants import *
from utils.pictures.paddle_pictures import *
from utils.RectButton import RectButton
from game.GameSettup import currentGameSettings

import pygame



IMAGE_SIZE = (200, 150)
IMAGE_SIZE_SMALL = (150, 100)

SMALL_PICTURE_XPOS = SCREEN_HEIGHT - 3 * SCREEN_HEIGHT / 10 + 40
SMALL_PICTURE_YPOS_LEFT = SCREEN_WIDTH / 2 - 250
SMALL_PICTURE_YPOS_RIGHT = SCREEN_WIDTH / 2 + 250

CENTER_PICTURE_XPOS = SCREEN_HEIGHT - 3 * SCREEN_HEIGHT / 10
CENTER_PICTURE_YPOS = SCREEN_WIDTH / 2


# Medium size picture for the selected picture in the gameSettings
imageDefaultMedium =  pygame.transform.scale(DEFAULT_PADDLE_PNG, IMAGE_SIZE)
imagePurlpleMedium = pygame.transform.scale(PURPLE_PADDLE_PNG, IMAGE_SIZE)
imageBlueMedium = pygame.transform.scale(BLUE_PADDLE_PNG, IMAGE_SIZE)

# Small size picture for the pictures that are not curently selected in gameSettings
imageDefaultSmall = pygame.transform.scale(DEFAULT_PADDLE_PNG, IMAGE_SIZE_SMALL)
imagePurpleSmall = pygame.transform.scale(PURPLE_PADDLE_PNG, IMAGE_SIZE_SMALL)
imageBlueSmall = pygame.transform.scale(BLUE_PADDLE_PNG, IMAGE_SIZE_SMALL)

#Add more maps to left or right as tuple of small medium and the img itself
imageListOneRight = [(imageBlueSmall, imageBlueMedium, BLUE_PADDLE_PNG)]
imageListOneLeft = [(imagePurpleSmall, imagePurlpleMedium, PURPLE_PADDLE_PNG)]

imageListTwoRight = [(imageBlueSmall, imageBlueMedium, BLUE_PADDLE_PNG)]
imageListTwoLeft = [(imagePurpleSmall, imagePurlpleMedium, PURPLE_PADDLE_PNG)]


currentImageOne = (imageDefaultSmall, imageDefaultMedium , DEFAULT_PADDLE_PNG)
currentImageTwo = (imageDefaultSmall, imageDefaultMedium , DEFAULT_PADDLE_PNG)

paddleOne = RectButton(SCREEN, CENTER_PICTURE_XPOS, CENTER_PICTURE_YPOS, imageDefaultMedium)
paddleLeftOne = RectButton(SCREEN, SMALL_PICTURE_XPOS, SMALL_PICTURE_YPOS_LEFT, imagePurpleSmall)
paddleRightOne = RectButton(SCREEN, SMALL_PICTURE_XPOS, SMALL_PICTURE_YPOS_RIGHT, imageBlueSmall)

paddleTwo = RectButton(SCREEN, CENTER_PICTURE_XPOS, CENTER_PICTURE_YPOS, imageDefaultMedium)
paddleLeftTwo = RectButton(SCREEN, SMALL_PICTURE_XPOS, SMALL_PICTURE_YPOS_LEFT, imagePurpleSmall)
paddleRightTwo = RectButton(SCREEN, SMALL_PICTURE_XPOS, SMALL_PICTURE_YPOS_RIGHT, imageBlueSmall)


class PlayerMenu:
    def __init__(self, paddleSelectOne, paddleSelectTwo):
        self.paddleSelectOne = paddleSelectOne
        self.paddleSelectTwo = paddleSelectTwo

    def changeWithLeftPaddle(self, id):
        if id == 1:
            self.paddleSelectOne.changeWithLeft(id)
        if id == 2:
            self.paddleSelectTwo.changeWithLeft(id)    

    def changeWithRightPaddle(self, id):
        if id == 1:
            self.paddleSelectOne.changeWithRight(id)
        if id == 2:
            self.paddleSelectTwo.changeWithRight(id)
    
    def draw(self, id):
        if id == 1:
            self.paddleSelectOne.draw()
        if id == 2:
            self.paddleSelectTwo.draw()
            
            

class PaddleSelect:
    def __init__(self, imageListLeft, imageListRight, curImg,
                 paddleSelect, paddleLeft, paddleRight):
        self.imageListLeft = imageListLeft
        self.imageListRight = imageListRight
        self.curImg = curImg
        self.paddleSelect = paddleSelect
        self.paddleLeft = paddleLeft
        self.paddleRight = paddleRight
        
    def changeWithLeft(self, id):
        if not self.imageListLeft:
            return
        
        newImage = self.imageListLeft.pop(0)
        self.imageListRight.insert(0, self.curImg)
        self.imageListLeft.append(self.imageListRight.pop(len(self.imageListRight) - 1))
        self.curImg = newImage
        
        self.paddleSelect.changeButtonImg(self.curImg[1])
        self.paddleLeft.changeButtonImg(self.imageListLeft[0][0])
        self.paddleRight.changeButtonImg(self.imageListRight[0][0])
        
        currentGameSettings.changePlayerPaddleImg(id, self.curImg[2])


    def changeWithRight(self, id):
        if not self.imageListRight:
            return

        newImage = self.imageListRight.pop(0)
        self.imageListLeft.insert(0, self.curImg)
        self.imageListRight.append(self.imageListLeft.pop(len(self.imageListLeft) - 1))
        self.curImg = newImage

        self.paddleSelect.changeButtonImg(self.curImg[1])
        self.paddleLeft.changeButtonImg(self.imageListLeft[0][0])
        self.paddleRight.changeButtonImg(self.imageListRight[0][0])
        
        currentGameSettings.changePlayerPaddleImg(id, self.curImg[2])
    
    def draw(self):
        self.paddleSelect.drawButton()
        self.paddleLeft.drawButton()
        self.paddleRight.drawButton()
        


paddleSelectOne = PaddleSelect(imageListOneLeft, imageListOneRight, currentImageOne,
                               paddleOne, paddleLeftOne, paddleRightOne)
paddleSelectTwo = PaddleSelect(imageListTwoLeft, imageListTwoRight, currentImageTwo,
                               paddleTwo, paddleLeftTwo, paddleRightTwo)

playerPaddleSelection = PlayerMenu(paddleSelectOne, paddleSelectTwo)


__all__ = ['playerPaddleSelection']
