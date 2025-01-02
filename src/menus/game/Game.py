import pygame
from utils.constants.MenuConstants import *
from utils.pictures.countdown_pictures import COUNTDOWN
from utils.fonts.Fonts import PRESS_START_2P
from utils.colors.Colors import YELLOW, RED
from utils.TextButton import TextButton
import math

SECONDS_FOR_DEATHMATCH = 30

class Game:
	def __init__(self, currentGameSettings):
		self.tableImg = currentGameSettings.currentTableImg
		self.playerOne = currentGameSettings.playerOne
		self.playerTwo = currentGameSettings.playerTwo
		self.puck = currentGameSettings.puck
		self.time = currentGameSettings.time # time is in seconds
		self.timePlayed = 0
		self.timeText = TextButton(SCREEN, 30, SCREEN_WIDTH / 2, self.returnTimeText(self.time), PRESS_START_2P, 30, YELLOW)
		self.scoreText = TextButton(SCREEN, 690, SCREEN_WIDTH / 2,  f"{self.playerOne.score} - {self.playerTwo.score}", PRESS_START_2P, 30, YELLOW)
		self.playerOneName = TextButton(SCREEN, 30, 300, self.playerOne.name, PRESS_START_2P, 30, YELLOW)
		self.playerTwoName = TextButton(SCREEN, 30, 1000, self.playerTwo.name, PRESS_START_2P, 30, YELLOW)

	def returnTimeText(self, time : int) -> str:
		minutes = math.floor(time / 60)
		seconds = time % 60
		if seconds < 10:
			return f"0{minutes}:0{seconds}"
		else:
			return f"0{minutes}:{seconds}"
	
	
	def beginningTimer(self):
		currentImageIndex = 0
		lastSwitchTime = pygame.time.get_ticks()
		
		running = True
		while running:
			SCREEN.blit(self.tableImg, (0, 0))
			self.timeText.displayText()
			self.scoreText.displayText()
			self.playerOneName.displayText()
			self.playerTwoName.displayText()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			# Get the current time
			currentTime = pygame.time.get_ticks()

			# Check if 1 second has passed since the last switch
			if currentTime - lastSwitchTime >= 1000:
				currentImageIndex += 1
				if currentImageIndex >= len(COUNTDOWN):
					currentImageIndex = 0
				lastSwitchTime = currentTime

			SCREEN.blit(COUNTDOWN[currentImageIndex], (0, 0))

			pygame.display.flip()

			
			if currentImageIndex == len(COUNTDOWN) - 1:
				pygame.time.wait(1000)
				running = False

	def start(self):
		'''Start the game and handle the game loop'''
		self.resetGame()
		self.beginningTimer()

		startTime = round(pygame.time.get_ticks() / 1000)
		running = True
		while running:
			self.timePlayed = round(pygame.time.get_ticks() / 1000) - startTime
			self.timeText.changeText(self.returnTimeText(self.time - self.timePlayed))

			if self.timePlayed == self.time:
				# If the score is tied, the game goes into sudden death mode
				if self.playerOne.score == self.playerTwo.score:
					self.suddenDeath()
				else:
					self.showWinner()
				break

			if (self.time - self.timePlayed <= SECONDS_FOR_DEATHMATCH):
				self.timeText.changeColour(RED)

			# Check if the game should continue
			running = self.eventContinueGame()

			self.handlePlayerControls(self.playerOne)
			self.handlePlayerControls(self.playerTwo)         

			self.updatePuckPosition()

			# Verify if the puck is in the gate area and it's a goal
			if self.puck.goalVerify(self.playerOne, self.playerTwo):
				self.updateScore()

			self.renderGame()

	def eventContinueGame(self):
		'''Check if the game should continue or if a player
		has pressed some keys to exit the game'''

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				return False
		return True

	def handlePlayerControls(self, player):
		'''Handle the player's controls'''
		keys = pygame.key.get_pressed()

		# Update position of the paddle
		if keys[player.controls[0]]:
			player.paddle.moveLeft()
		if keys[player.controls[1]]:
			player.paddle.moveRight()
		if keys[player.controls[2]]:
			player.paddle.moveUp()
		if keys[player.controls[3]]:
			player.paddle.moveDown()

	def updatePuckPosition(self):
		'''Update the puck's position and check for collisions'''
		self.puck.move()
		self.puck.collision(self.playerOne.paddle)
		self.puck.collision(self.playerTwo.paddle)

	def renderGame(self):
		'''Update the game on the screen and every element in it'''
		SCREEN.blit(self.tableImg, (0, 0))
		self.timeText.displayText()
		self.scoreText.displayText()
		self.playerOneName.displayText()
		self.playerTwoName.displayText()
		self.playerOne.paddle.draw()
		self.playerTwo.paddle.draw()
		self.puck.draw()
		pygame.display.update()

	def resetGame(self):
		'''Reset the game to its initial state'''
		self.playerOne.paddle.resetPosition()
		self.playerTwo.paddle.resetPosition()
		self.puck.resetPosition()
		self.resetScore()

	def resetScore(self):
		'''Reset the score of the players'''
		self.playerOne.score = 0
		self.playerTwo.score = 0
		self.updateScore()
	
	def updateScore(self):
		'''Update the score of the players and display it'''
		self.scoreText.changeText(f"{self.playerOne.score} - {self.playerTwo.score}")
		self.scoreText.displayText()

	def suddenDeath(self):
		'''After the timer ends, if the score is tied, the game goes into sudden death mode
		This means that the first player to score wins the game'''
		self.resetGame()
		self.scoreText.changeText("First to score wins!")
		self.scoreText.changeColour(RED)
		self.timeText.changeText("Sudden Death")
		self.timeText.changeColour(RED)
		
		while True:
			if not self.eventContinueGame():
				break

			self.handlePlayerControls(self.playerOne)
			self.handlePlayerControls(self.playerTwo)
			self.updatePuckPosition()
			self.renderGame()

			# In sudden death mode, the winner is the player who scores first
			# Golden goal rule
			if self.puck.goalVerify(self.playerOne, self.playerTwo):
				self.showWinner()
				break

	def showWinner(self):
		'''Show the winner of the game on the screen'''
		if self.playerOne.score > self.playerTwo.score:
			winner = self.playerOne.name
		elif self.playerOne.score < self.playerTwo.score:
			winner = self.playerTwo.name

		winnerText = TextButton(SCREEN, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, f"{winner} Wins!", PRESS_START_2P, 50, YELLOW)
		SCREEN.fill((0, 0, 0))  # Black background
		winnerText.displayText()
		pygame.display.update()
		pygame.time.wait(3000) # Show the winner for 3 seconds


__all__ = ['Game']