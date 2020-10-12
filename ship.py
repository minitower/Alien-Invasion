import pygame
import os
from pygame.sprite import Sprite

current_path = os.path.dirname (__file__)
resource_path = os.path.join (current_path, 'res')

image = pygame.image.load (os.path.join (resource_path, 'rocket-2442125.png'))
scale = pygame.transform.scale(image, (image.get_width()//9, image.get_height()//9))

class Ship():

    def __init__(self, ai_setings, screen):
        self.screen = screen
        self.ai_setings = ai_setings
        self.image = scale
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.center = float(self.rect.centerx)

    def update (self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setings.ship_speed_factor
        if self.moving_up and self.rect.top >0:
            self.rect.centery -=1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery +=1
        self.rect.centerx = self.center

    def blitme (self):
        self.screen.blit (self.image, self.rect)

    def center_ship (self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
