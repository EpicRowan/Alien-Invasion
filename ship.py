import pygame

class Ship:
	""" A class to manage the ship"""
	# Gives ship access to all the game resources defined in AlienInvasion
	def __init__(self, ai_game):
		"""Initialize the ship and set starting position"""
		# assign the screen to an attribute of Ship
		self.screen = ai_game.screen
		# Access the screen's rectangle to place ship in current location
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings
		# Load the ship image and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Start each new ship at the bottom center
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

		#Movement flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		'''Update the ships position based on the movement flag'''
		# if the x coordinate of the right edge is less than self.screen_rect, the ship hasnt reached right edge
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		# if the balue of the left side of rect is > 0, ship isnt at the left edge	
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship at it's current location """
		self.screen.blit(self.image, self.rect)