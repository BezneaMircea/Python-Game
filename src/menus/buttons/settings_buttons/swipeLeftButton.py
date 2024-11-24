import pygame

from utils.pictures.buttons_pictures import *
from utils.constants.MenuConstants import *
from utils.RectButton import RectButton
from buttons.settings_buttons.MapSelect import (
    SMALL_PICTURE_YPOS_LEFT,
    SMALL_PICTURE_XPOS,
)


xPosPlay = SMALL_PICTURE_XPOS
yPosPlay = SMALL_PICTURE_YPOS_LEFT - 120

swipeLeftButton = RectButton(SCREEN, xPosPlay, yPosPlay, SWIPE_LEFT_BUTTON_PNG)

__all__ = ['swipeLeftButton']