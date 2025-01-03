from utils.constants.MenuConstants import *
from utils.pictures.gate_picture import *

class Gate():
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.imageRect = self.image.get_rect(center=(x, y))

    def draw(self):
        self.imageRect = self.image.get_rect(center=(self.x, self.y))
        self.screen.blit(self.image, self.imageRect)

gateLeft = Gate(SCREEN, GATE_LEFT_POSITION[0], GATE_LEFT_POSITION[1], GATE_PNG)
gateRight = Gate(SCREEN, GATE_RIGHT_POSITION[0], GATE_RIGHT_POSITION[1], GATE_PNG)

__all__ = ['gateLeft', 'gateRight']