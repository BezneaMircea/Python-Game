from utils.pictures.table_pictures import *
from game.Player import *
from game.Puck import *

CURRENT_MAP = DEFAULT_TABLE_PNG

class GameSetup:
    def __init__(self, currentTableImg, playerOne,
                 playerTwo, puck, time):
        self.currentTableImg = currentTableImg
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.puck = puck
        self.time = time

    def changeTable(self, newTableImg):
        self.currentTableImg = newTableImg
    
    def changePlayerPaddleImg(self, playerId, newImg):
        if playerId == 1:
            self.playerOne.changePlayerPaddle(newImg)
            return    
        if playerId == 2:
            self.playerTwo.changePlayerPaddle(newImg)
            return
        IndexError


time = 150

currentGameSettings = GameSetup(DEFAULT_TABLE_PNG, playerOne,
                                 playerTwo, puck, time)

__all__ = ['currentGameSettings']