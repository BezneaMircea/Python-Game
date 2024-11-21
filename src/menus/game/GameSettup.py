from utils.pictures.Pictures import *

CURRENT_MAP = SEA_TABLE_PNG

class GameSettup:
    def __init__(self, currentTableImg, playerOne,
                 playerTwo, puckImg, time):
        self.currentTableImg = currentTableImg
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.puckImg = puckImg
        self.time = time
    
    