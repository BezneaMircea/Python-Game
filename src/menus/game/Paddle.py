from utils.constants.MenuConstants import *
from utils.pictures.paddle_pictures import *
from game.Puck import *
import math

# Paddle radius
PADDLE_RADIUS = BLUE_PADDLE_PNG.get_width() // 2

# Initial paddle speed
INITIAL_PADDLE_SPEED = 7

# Starting point for the paddles
DISTANCE_FROM_CENTER = 500

# Paddle margins
TABLE_SIDE_WALLS = 105
TABLE_TOP_WALLS = 140
PADDLE_CENTER_MARGIN = 57
MARGINS_ONE = (TABLE_SIDE_WALLS, SCREEN_WIDTH / 2 - PADDLE_CENTER_MARGIN,
               TABLE_TOP_WALLS, SCREEN_HEIGHT - TABLE_TOP_WALLS)
MARGINS_TWO = (SCREEN_WIDTH / 2 + PADDLE_CENTER_MARGIN, SCREEN_WIDTH - TABLE_SIDE_WALLS,
               TABLE_TOP_WALLS, SCREEN_HEIGHT - TABLE_TOP_WALLS)

class Paddle():
    def __init__(self, screen, x, y, radius, image, speed, margins):
        """Constructor for the paddle class
            margins = (marginLeft, marginRight, marginUp, marginBottom)
        """
        self.screen = screen
        self.startingX = x
        self.startingY = y
        self.x = x
        self.y = y
        self.radius = radius
        self.image = image
        self.imageRect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.margins = margins

    def resetPosition(self):
        self.x = self.startingX
        self.y = self.startingY

    def moveLeft(self):
        # Verific daca paleta va intra in coliziune cu pucul la stanga
        if not self.isCollidingWithPuck(-self.speed, 0):
            self.x -= self.speed
            self.canMove()

    def moveRight(self):
        # Verific daca paleta va intra in coliziune cu pucul la dreapta
        if not self.isCollidingWithPuck(self.speed, 0):
            self.x += self.speed
            self.canMove()

    def moveUp(self):
        # Verific daca paleta va intra in coliziune cu pucul sus
        if not self.isCollidingWithPuck(0, -self.speed):
            self.y -= self.speed
            self.canMove()

    def moveDown(self):
        # Verific daca paleta va intra in coliziune cu pucul jos
        if not self.isCollidingWithPuck(0, self.speed):
            self.y += self.speed
            self.canMove()

    def canMove(self):
        self.x = max(self.margins[0], min(self.x, self.margins[1]))
        self.y = max(self.margins[2], min(self.y, self.margins[3]))

    def draw(self):
        self.imageRect = self.image.get_rect(center=(self.x, self.y))
        self.screen.blit(self.image, self.imageRect)

    def isCollidingWithPuck(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        
        # Calculam distanta dintre paleta noua și puc
        dist = math.sqrt((new_x - puck.x) ** 2 + (new_y - puck.y) ** 2)

        # Daca distanta dintre paleta și puc este mai mica decat suma razelor lor, exista coliziune
        return dist < self.radius + puck.radius

    def changeImg(self, newImg):
        self.image = newImg
        self.imageRect = self.image.get_rect(center=(self.x, self.y))

paddleOne = Paddle(SCREEN, SCREEN_WIDTH / 2 - DISTANCE_FROM_CENTER, SCREEN_HEIGHT / 2, PADDLE_RADIUS,
                   DEFAULT_PADDLE_PNG, INITIAL_PADDLE_SPEED, MARGINS_ONE)

paddleTwo = Paddle(SCREEN, SCREEN_WIDTH / 2 + DISTANCE_FROM_CENTER, SCREEN_HEIGHT / 2, PADDLE_RADIUS,
                   DEFAULT_PADDLE_PNG, INITIAL_PADDLE_SPEED, MARGINS_TWO)

__all__ = ['paddleOne', 'paddleTwo']