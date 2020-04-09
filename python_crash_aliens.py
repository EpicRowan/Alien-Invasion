import sys
import pygame 
from settings import Settings
from ship import Ship
from bullet import Bullet 

class AlienInvasion:
	"""Class to manage game assets and behavior"""

	def __init__(self):

		"""Initialize the game and create resources"""

		pygame.init()
		self.settings = Settings()
		# Initializes the background settings
		# Create a display window with a tuple that defines the dimensions of the game window
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		# self.screen = 'a surface = a part of the screen when a game can be played'
		# when the game is activated, the surface will be redrawn on every pass through the loop and updated
		pygame.display.set_caption("Alien Invasion")
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		
	def run_game(self):
		""" Start the main loop for the game """
		while True:
			self.check_events()
			"""Watch for keyboard and mouse events"""
			self.ship.update()
			self.update_screen()
			self.bullets.update()
			# to make the program respond to events, we write an event loop
	def check_events(self):
		# pygame.event.get() = a function that returns a list of events that have taken place since the last time the function was called 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		'''Respond to key presses''' 
		if event.key == pygame.K_RIGHT:
			# Move the ship right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			# Move the ship left
			self.ship.moving_left = True
		elif event.key == pygame.K_SPACE:
			# Fire bullets on space bar
			self._fire_bullet()

	def _check_keyup_events(self, event):
		'''Respond to key releasing''' 
		if event.key == pygame.K_RIGHT:
			# Stop the ship moving right
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			# Stop the ship moving left
			self.ship.moving_left = False

	def _fire_bullet(self):
		'''Create a new bullet and add to the bullets group'''
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)

	def update_screen(self):
		# redraw the screen each pass of the lopp
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		# tells Python to make the most recently drawn screen visible 			
		pygame.display.flip()
			
if __name__ == '__main__':
	# Make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()