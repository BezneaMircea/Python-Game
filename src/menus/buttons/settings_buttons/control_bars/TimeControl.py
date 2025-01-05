from utils.pictures.buttons_pictures import BARA_PNG, SCROLL_BUTTON_PNG
from utils.constants.MenuConstants import *
from utils.fonts.Fonts import PRESS_START_2P
from utils.colors.Colors import *
from menus.buttons.settings_buttons.control_bars.ControlBar import ControlBar
from game.GameSetup import currentGameSettings
from utils.RectButton import RectButton
from utils.TextButton import TextButton
import math

X_POS = SCREEN_HEIGHT / 4
Y_POS = SCREEN_WIDTH / 2


bar = RectButton(SCREEN, X_POS, Y_POS, BARA_PNG)
barButton = RectButton(SCREEN, X_POS, Y_POS, SCROLL_BUTTON_PNG)
textButton = TextButton(SCREEN, X_POS, Y_POS - 320, "Time:", PRESS_START_2P, 30, PURPLE)
valueButton = TextButton(SCREEN, X_POS, Y_POS + 320, "02:30", PRESS_START_2P, 20, PURPLE)


class TimeControlBar(ControlBar):
    # originalValue should be given as seconds if we are talking about time
    def __init__(self, bar, barButton, textButton, leftMax,
                 rightMax, valueButton, originalValue, maxValue, minValue):
        super().__init__(bar, barButton, textButton, leftMax, rightMax, valueButton,
                       originalValue, maxValue, minValue)


    def changeValueToText(self):
        self.computeValue()
        currentGameSettings.time = self.currentValue
        minutes = math.floor(self.currentValue / 60)
        seconds = self.currentValue % 60
        if seconds < 10:
            self.valueButton.changeText(f"0{minutes}:0{seconds}")
        else:
            self.valueButton.changeText(f"0{minutes}:{seconds}")
    
    def computeValue(self):
        self.currentValue = self.originalValue + round((self.unit * (self.barButton.yPos - self.originalPos)))


    def performAction(self, mouseCoord):
        pass

    
    
timeControl = TimeControlBar(bar, barButton, textButton, Y_POS - 230, Y_POS + 230, valueButton, 150, 240, 60)



__all__ = ['timeControl']