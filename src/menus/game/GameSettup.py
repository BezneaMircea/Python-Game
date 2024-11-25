from utils.pictures.table_pictures import *

CURRENT_MAP = DEFAULT_TABLE_PNG

class GameSettup:
    def __init__(self, currentTableImg, playerOne,
                 playerTwo, puckImg, time):
        self.currentTableImg = currentTableImg
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.puckImg = puckImg
        self.time = time

    def changeTable(self, newTableImg):
        self.currentTableImg = newTableImg

__all__ = ['GameSettup']


# TODO:
# Create the player class and so on
# eg: class player():
#       self.name = name
#       self.puck = puck
#       self.controls = (leftKey, rightKey, upKey, downKey)
# Change de default values for players, puckImg, time

#Random values so i can initialize the class
playerOne = 1
playerTwo = 2
puckImg = 3
time = 4

#
currentGameSettings = GameSettup(DEFAULT_TABLE_PNG, playerOne,
                                 playerTwo, puckImg, time)

__all__ = ['currentGameSettings']