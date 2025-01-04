from utils.pictures.buttons_pictures import *
from utils.constants.MenuConstants import *
from utils.RectButton import RectButton
from menus.buttons.settings_buttons.MapSelect import (
    SMALL_PICTURE_YPOS_RIGHT,
    SMALL_PICTURE_XPOS
)


xPosPlay = SMALL_PICTURE_XPOS
yPosPlay = SMALL_PICTURE_YPOS_RIGHT + 120

swipeRightButton = RectButton(SCREEN, xPosPlay, yPosPlay, SWIPE_RIGHT_BUTTON_PNG)

__all__ = ['swipeRightButton']