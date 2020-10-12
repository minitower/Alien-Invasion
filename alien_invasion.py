import sys
import pygame
from Setting import Setting
from ship import *
import game_function as gf
from pygame.sprite import Group
from alien import *
from game_stats import *
from button import *
from scoreboard import *
from Setting_button import *


def run_game():
    pygame.init()
    pygame.display.set_caption ('Alien Invasion')
    ai_setings = Setting()
    screen = pygame.display.set_mode ((ai_setings.screen_width,
                                        ai_setings.screen_height), pygame.FULLSCREEN)
    play_button = Button (ai_setings, screen, 'Play')
    setting_button = S_Button (ai_setings, screen, 'Setting')
    q_button = Q_Button (ai_setings, screen, 'Quit')
    ship = Ship (ai_setings, screen)
    bullet = Group ()
    alien = Alien (ai_setings, screen, scale)
    aliens = Group()
    gf.create_fleet (ai_setings, screen, ship, aliens)
    stats = GameStats (ai_setings)
    sb = scoreboard (ai_setings, screen, stats)
    gf.update_screen(ai_setings, screen, stats, sb, ship, bullet, aliens,
    play_button, setting_button, q_button)

    while True:
        gf.check_events(ai_setings, screen, stats, sb, play_button, setting_button,
        q_button, ship, aliens, bullet)
        if stats.game_active:
            ship.update ()
            gf.update_screen(ai_setings, screen, stats, sb, ship, bullet, aliens,
            play_button, setting_button, q_button)
            gf.update_bullet(ai_setings, screen, stats, sb, ship, bullet, aliens)
            gf.update_aliens (ai_setings, stats, screen, sb, ship, aliens, bullet)

run_game ()
