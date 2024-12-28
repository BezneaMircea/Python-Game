from utils.constants.MenuConstants import *
from utils.pictures.puck_pictures import *
import math

# Puck radius
PUCK_RADIUS = PUCK_DEFAULT_PNG.get_width() // 2

EPSILON = 2

# Initial puck speed
INITIAL_PUCK_SPEED = 10

# Puck margins
TABLE_SIDE_WALLS = 90
TABLE_TOP_WALLS = 125
MARGINS = (TABLE_SIDE_WALLS, SCREEN_WIDTH - TABLE_SIDE_WALLS,	
		   TABLE_TOP_WALLS, SCREEN_HEIGHT - TABLE_TOP_WALLS)

class Puck():
	def __init__(self, screen, x, y, dx, dy, radius, image, speed, margins):
		"""Constructor for the puck class
			margins = (marginLeft, marginRight, marginUp, marginBottom)
		"""
		self.screen = screen
		self.startingX = x
		self.startingY = y
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.radius = radius
		self.image = image
		self.imageRect = self.image.get_rect(center=(x, y))
		self.speed = speed
		self.margins = margins

	def resetPosition(self):
		self.x = self.startingX
		self.y = self.startingY
		self.dx = 0
		self.dy = 0

	def collision(self, object):
		"""Check if the puck collided with a paddle"""
		dist = ((self.x - object.x) ** 2 + (self.y - object.y) ** 2) ** 0.5
		if dist <= self.radius + object.radius + EPSILON:
			collision_angle = math.atan2(self.y - object.y, self.x - object.x)

			self.dx = math.cos(collision_angle) * self.speed
			self.dy = math.sin(collision_angle) * self.speed

		if abs(self.dx) < 1:
			self.dx = -self.dx
	
		if abs(self.dy) < 1:
			self.dy = -self.dy

	def move(self):
		self.x += self.dx
		self.y += self.dy

		# Coliziuni cu marginile din stanga și dreapta
		if self.x - self.radius <= self.margins[0] or self.x + self.radius >= self.margins[1]:
			self.dx = -self.dx  # Inversam directia pe axa X
			# Impingem pucul putin departe de marginea mesei pentru a preveni statul
			if self.x - self.radius <= self.margins[0]:
				self.x = self.margins[0] + self.radius
			elif self.x + self.radius >= self.margins[1]:
				self.x = self.margins[1] - self.radius

		# Coliziuni cu marginile de sus și jos
		if self.y - self.radius <= self.margins[2] or self.y + self.radius >= self.margins[3]:
			self.dy = -self.dy  # Inversam directia pe axa Y
			# Impingem pucul putin departe de marginea mesei pentru a preveni statul
			if self.y - self.radius <= self.margins[2]:
				self.y = self.margins[2] + self.radius
			elif self.y + self.radius >= self.margins[3]:
				self.y = self.margins[3] - self.radius

		# Ne asiguram ca pucul nu depaseste limitele mesei
		self.canMove()
		

	def canMove(self):
		self.x = max(self.margins[0], min(self.x, self.margins[1]))
		self.y = max(self.margins[2], min(self.y, self.margins[3]))

	def draw(self):
		self.imageRect = self.image.get_rect(center=(self.x, self.y))
		self.screen.blit(self.image, self.imageRect)

puck = Puck(SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0, PUCK_RADIUS, PUCK_DEFAULT_PNG, INITIAL_PUCK_SPEED, MARGINS)

__all__ = ['puck']