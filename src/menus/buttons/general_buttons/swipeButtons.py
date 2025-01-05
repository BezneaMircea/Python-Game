from utils.pictures.buttons_pictures import *
from utils.constants.MenuConstants import *
from utils.RectButton import RectButton
from menus.buttons.settings_buttons.MapSelect import mapSelection
from menus.buttons.player_settings_buttons.PaddleSelect import paddleSelectOne, paddleSelectTwo
from menus.buttons.settings_buttons.MapSelect import (
    SMALL_PICTURE_YPOS_RIGHT,
    SMALL_PICTURE_XPOS,
    SMALL_PICTURE_YPOS_LEFT
)


class SwipeButton(RectButton):
    def __init__(self, screen, xPos, yPos, image, imageBig):
        super().__init__(screen, xPos, yPos, image)
        self.imageSmall = image
        self.imageBig = imageBig
        
    
    def interactWithCursor(self, mouseCoord):
        if (self.isCursorOn(mouseCoord)):
            self.changeButtonImg(self.imageBig)
        else:
            self.changeButtonImg(self.imageSmall)


class SwipeButtonLeft(SwipeButton):
    def __init__(self, screen, xPos, yPos, image, imageBig, objectToSwipe):
        super().__init__(screen, xPos, yPos, image, imageBig)
        self.objectToSwipe = objectToSwipe
    
    def performAction(self, mouseCoord, pressed):
        if self.isCursorOn(mouseCoord) and pressed[0]:
            self.objectToSwipe.changeWithLeft()

class SwipeButtonRight(SwipeButton):
    def __init__(self, screen, xPos, yPos, image, imageBig, objectToSwipe):
        super().__init__(screen, xPos, yPos, image, imageBig)
        self.objectToSwipe = objectToSwipe
    
    def performAction(self, mouseCoord, pressed):
        if self.isCursorOn(mouseCoord) and pressed[0]:
            self.objectToSwipe.changeWithRight()


xPosPlayRight = SMALL_PICTURE_XPOS
yPosPlayRight = SMALL_PICTURE_YPOS_RIGHT + 120
swipeRightButton = SwipeButtonRight(SCREEN, xPosPlayRight, yPosPlayRight, SWIPE_RIGHT_BUTTON_PNG, SWIPE_RIGHT_BUTTON__BIG_PNG, mapSelection)
swipeRightButtonPlayerSettingsOne = SwipeButtonRight(SCREEN, xPosPlayRight, yPosPlayRight, SWIPE_RIGHT_BUTTON_PNG, SWIPE_RIGHT_BUTTON__BIG_PNG, paddleSelectOne)
swipeRightButtonPlayerSettingsTwo = SwipeButtonRight(SCREEN, xPosPlayRight, yPosPlayRight, SWIPE_RIGHT_BUTTON_PNG, SWIPE_RIGHT_BUTTON__BIG_PNG, paddleSelectTwo)

xPosPlayLeft = SMALL_PICTURE_XPOS
yPosPlayLeft = SMALL_PICTURE_YPOS_LEFT - 120
swipeLeftButton = SwipeButtonLeft(SCREEN, xPosPlayLeft, yPosPlayLeft, SWIPE_LEFT_BUTTON_PNG, SWIPE_LEFT_BUTTON_BIG_PNG, mapSelection)
swipeLeftButtonPlayerSettingsOne = SwipeButtonLeft(SCREEN, xPosPlayLeft, yPosPlayLeft, SWIPE_LEFT_BUTTON_PNG, SWIPE_LEFT_BUTTON_BIG_PNG, paddleSelectOne)
swipeLeftButtonPlayerSettingsTwo = SwipeButtonLeft(SCREEN, xPosPlayLeft, yPosPlayLeft, SWIPE_LEFT_BUTTON_PNG, SWIPE_LEFT_BUTTON_BIG_PNG, paddleSelectTwo)




__all__ = ['swipeRightButton', 'swipeLeftButton']