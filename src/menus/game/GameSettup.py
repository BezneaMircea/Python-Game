from utils.pictures.table_pictures import *
from game.Player import *
from game.Puck import *

CURRENT_MAP = DEFAULT_TABLE_PNG

class GameSettup:
    def __init__(self, currentTableImg, playerOne,
                 playerTwo, puck, time):
        self.currentTableImg = currentTableImg
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.puck = puck
        self.time = time

    def changeTable(self, newTableImg):
        self.currentTableImg = newTableImg

# TODO:
# Create the player class and so on
# eg: class player():
#       self.name = name
#       self.puck = puck
#       self.controls = (leftKey, rightKey, upKey, downKey)
# Change de default values for players, puckImg, time

time = 4

currentGameSettings = GameSettup(DEFAULT_TABLE_PNG, playerOne,
                                 playerTwo, puck, time)

__all__ = ['currentGameSettings']