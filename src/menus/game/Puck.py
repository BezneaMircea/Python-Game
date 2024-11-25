from utils.constants.MenuConstants import *
from utils.pictures.puck_pictures import *

# Puck radius
PUCK_RADIUS = PUCK_DEFAULT_PNG.get_width() // 2

EPSILON = 2

# Initial puck speed
INITIAL_PUCK_SPEED = 10

# Puck margins
TABLE_SIDE_WALLS = 105
TABLE_TOP_WALLS = 140
MARGINS = (TABLE_SIDE_WALLS, SCREEN_WIDTH - TABLE_SIDE_WALLS,
		   TABLE_TOP_WALLS, SCREEN_HEIGHT - TABLE_TOP_WALLS)

class Puck():
	def __init__(self, screen, x, y, radius, image, speed, margins):
		"""Constructor for the puck class
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

	def collision(self, object):
		"""Check if the puck collided with a paddle"""
		dist = ((self.x - object.x) ** 2 + (self.y - object.y) ** 2) ** 0.5
		if (dist <= self.radius + object.radius + EPSILON):
			return True
		return False

	def move(self):
		self.x += self.speed
		self.y += self.speed
		self.canMove()

	def canMove(self):
		self.x = max(self.margins[0], min(self.x, self.margins[1]))
		self.y = max(self.margins[2], min(self.y, self.margins[3]))

	def draw(self):
		self.imageRect = self.image.get_rect(center=(self.x, self.y))
		self.screen.blit(self.image, self.imageRect)

puck = Puck(SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PUCK_RADIUS, PUCK_DEFAULT_PNG, INITIAL_PUCK_SPEED, MARGINS)

__all__ = ['puck']