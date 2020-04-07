import sys
import pygame 

class AlienInvasion:
	"""Class to manage game assets and behavior"""

	def __init__(self):

		"""Initialize the game and create resources"""

		pygame.init()
		# Initializes the background settings
		# Create a display window with a tuple that defines the dimensions of the game window
		self.screen = pygame.display.set_mode((1200,800))
		# self.screen = 'a surface = a part of the screen when a game can be played'
		# when the game is activated, the surface will be redrawn on every pass through the loop and updated
		pygame.display.set_caption("Alien Invasion")
		# set the background color
		self.bg_color = (230,230,230)


	def run_game(self):
		""" Start the main loop for the game """
		while True:
			"""Watch for keyboard and mouse events"""
			# to make the program respond to events, we write an event loop

			# pygame.event.get() = a function that returns a list of events that have taken place since the last time the function was called 
			for event in pygame.event.get():
						if event.type == pygame.QUIT:
					sys.exit()
			# redraw the screen each pass of the lopp
			self.screen.fill(self.bg_color)

			# tells Python to make the most recently drawn screen visible 
			pygame.diplay.flip()
			

	if __name__ == '__main__':
		# Make a game instance and run the game
		ai = AlienInvasion()
		ai.run_game()