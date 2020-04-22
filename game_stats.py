class GameStats:
	"""Track stats for Alien Invasion"""
	def __init__(self, ai_game):
		"""Initialize stats"""
		self.settings = ai_game.settings
		self.reset_stats()

		# start game in an active state
		self.game_active = False

	def reset_stats(self):
		"""Initialize statistics that can change during game"""
		self.ships_left = self.settings.ship_limit