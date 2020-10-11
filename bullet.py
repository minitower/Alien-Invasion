import pygame
from pygame.sprite import Sprite

class Bullet (Sprite):
    def __init__(self, ai_setings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect (0,0,ai_setings.bullet_width,
        ai_setings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float (self.rect.y)

        self.collor = ai_setings.bullet_collor
        self.speed_factor = ai_setings.bullet_speed_factor

        self.shoot = False

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet (self):
        pygame.draw.rect (self.screen, self.collor, self.rect)
