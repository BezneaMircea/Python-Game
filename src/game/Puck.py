from utils.constants.MenuConstants import *
from utils.pictures.puck_pictures import *
import math

# Puck radius
PUCK_RADIUS = PUCK_DEFAULT_PNG.get_width() // 2

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

	def resetPlayerOnePuckPosition(self):
		self.x = POSITION_PUCK_PLAYER_ONE[0]
		self.y = POSITION_PUCK_PLAYER_ONE[1]
		self.dx = 0
		self.dy = 0

	def resetPlayerTwoPuckPosition(self):
		self.x = POSITION_PUCK_PLAYER_TWO[0]
		self.y = POSITION_PUCK_PLAYER_TWO[1]
		self.dx = 0
		self.dy = 0

	def collision(self, object):
		"""Check if the puck collided with a paddle"""
		dist = ((self.x - object.x) ** 2 + (self.y - object.y) ** 2) ** 0.5
		if dist <= self.radius + object.radius + EPSILON:
			collisionAngle = math.atan2(self.y - object.y, self.x - object.x)

			self.dx = math.cos(collisionAngle) * self.speed
			self.dy = math.sin(collisionAngle) * self.speed

	def move(self):
		# Colisions with left and right margins
		if self.x - self.radius <= self.margins[0] or self.x + self.radius >= self.margins[1]:
			self.dx = -self.dx  # Switch direction on the OX axis
			# Push the puck a little further from the table's edge to prevent it from standing still
			if self.x - self.radius <= self.margins[0]:
				self.x = self.margins[0] + self.radius
			elif self.x + self.radius >= self.margins[1]:
				self.x = self.margins[1] - self.radius

		# Colisions with top and bottom margins
		if self.y - self.radius <= self.margins[2] or self.y + self.radius >= self.margins[3]:
			self.dy = -self.dy  # Switch direction on the OY axis
			# Push the puck a little further from the table's edge to prevent it from standing still
			if self.y - self.radius <= self.margins[2]:
				self.y = self.margins[2] + self.radius
			elif self.y + self.radius >= self.margins[3]:
				self.y = self.margins[3] - self.radius

		self.x += self.dx
		self.y += self.dy

		# We make sure the puck doesn't exceed the table's limits
		self.canMove()
		
	def canMove(self):
		self.x = max(self.margins[0], min(self.x, self.margins[1]))
		self.y = max(self.margins[2], min(self.y, self.margins[3]))

	def goalVerify(self, playerOne, playerTwo):
		"""Check if the puck enters a goal and handle the state changes."""
		isGoal = False
		if GOAL_TOP <= self.y <= GOAL_BOTTOM:
			if self.x - self.radius <= self.margins[0]:
				playerTwo.increaseScore()
				
				playerOne.paddle.resetPosition()
				playerTwo.paddle.resetPosition()
				
				self.resetPlayerOnePuckPosition()
				isGoal = True
				# Goal for Player 2
				# Increment Player 2's score
			elif self.x + self.radius >= self.margins[1]:
				playerOne.increaseScore()

				playerOne.paddle.resetPosition()
				playerTwo.paddle.resetPosition()

				self.resetPlayerTwoPuckPosition()
				# Goal for Player 1
				# Increment Player 1's score
				isGoal = True
		return isGoal

	def draw(self):
		self.imageRect = self.image.get_rect(center=(self.x, self.y))
		self.screen.blit(self.image, self.imageRect)

puck = Puck(SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0, PUCK_RADIUS, PUCK_DEFAULT_PNG, INITIAL_PUCK_SPEED, MARGINS)

__all__ = ['puck']