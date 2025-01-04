from utils.pictures.buttons_pictures import BARA_PNG, SCROLL_BUTTON_PNG
from utils.constants.MenuConstants import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.colors.Colors import *
from menus.buttons.settings_buttons.control_bars.ControlBar import ControlBar
from utils.RectButton import RectButton
from utils.TextButton import TextButton
import pygame

X_POS = SCREEN_HEIGHT / 4
Y_POS = SCREEN_WIDTH / 2

DISTANCE_BEETWEEN_BARS = 80

volumeBar = RectButton(SCREEN, X_POS + DISTANCE_BEETWEEN_BARS, Y_POS, BARA_PNG)
volumeButton = RectButton(SCREEN, X_POS + DISTANCE_BEETWEEN_BARS, Y_POS, SCROLL_BUTTON_PNG)
volumeText = TextButton(SCREEN, X_POS + DISTANCE_BEETWEEN_BARS, Y_POS - 320, 'Volume:', PRESS_START_2P, 24, PURPLE)
volumeValueButton = TextButton(SCREEN, X_POS + DISTANCE_BEETWEEN_BARS, Y_POS + 300, "0.50", PRESS_START_2P, 20, PURPLE)


class VolumeControlBar(ControlBar):
    # originalValue should be given as seconds if we are talking about time
    def __init__(self, bar, barButton, textButton, leftMax,
                 rightMax, valueButton, originalValue, maxValue, minValue):
        super().__init__(bar, barButton, textButton, leftMax, rightMax, valueButton,
                       originalValue, maxValue, minValue)


    def changeValueToText(self):
        self.computeValue()
        #Add Volume field to currentGameSettings here
        if self.currentValue == self.maxValue:
            self.valueButton.changeText("MAX")
            return

        if (self.currentValue == self.minValue):
            self.valueButton.changeText("MIN")
            return

        if (self.currentValue * 100) % 10 == 0:
            self.valueButton.changeText(f"{self.currentValue}0")
        else:
            self.valueButton.changeText(f"{self.currentValue}")

    def computeValue(self):
        self.currentValue = round(self.originalValue + self.unit * (self.barButton.yPos - self.originalPos), 2)
        pygame.mixer.music.set_volume(self.currentValue)
            
volumeControl = VolumeControlBar(volumeBar, volumeButton, volumeText, Y_POS - 230, Y_POS + 230, volumeValueButton, 0.5, 1, 0)

__all__ = ['volumeControl']