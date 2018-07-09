import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
	"""A class to represent your ship."""

	def __init__(self, ai_settings, screen):
		"""Initialise the ship and set its starting position."""
		super().__init__()

		self.screen = screen
		self.ai_settings = ai_settings

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom centre of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship's centre.
		self.centre = float(self.rect.centerx)

		# Movement flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ship's position based on movement flags."""
		# Update the ship's centre value, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centre += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centre -= self.ai_settings.ship_speed_factor

		# Update rect object from self.centre.
		self.rect.centerx = self.centre

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	def centre_ship(self):
		"""Centre the ship on the screen."""
		self.centre = self.screen_rect.centerx
