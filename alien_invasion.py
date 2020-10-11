import sys
import pygame
from Setting import Setting
from ship import *
import game_function as gf
from pygame.sprite import Group
from alien import *
from game_stats import *
from button import *


def run_game():
    pygame.init()
    pygame.display.set_caption ('Alien Invasion')
    ai_setings = Setting()
    screen = pygame.display.set_mode ((ai_setings.screen_width,
                                        ai_setings.screen_height))
    play_button = Button (ai_setings, screen, 'Play')
    ship = Ship (ai_setings, screen)
    bullet = Group ()
    alien = Alien (ai_setings, screen, scale)
    aliens = Group()
    gf.create_fleet (ai_setings, screen, ship, aliens)
    stats = GameStats (ai_setings)

    while True:
        gf.check_events(ai_setings, screen, ship, bullet)
        gf.update_screen(ai_setings, screen, stats, ship, bullet, aliens, play_button)
        if stats.game_active:
            ship.update ()
            gf.update_screen(ai_setings, screen, stats, ship, bullet, aliens, play_button)
            gf.update_bullet(ai_setings, screen, ship, bullet, aliens)
            gf.update_aliens (ai_setings, stats, screen, ship, aliens, bullet)
            print ('Hi')
run_game ()
