import sys
import pygame
from Setting import Setting
from bullet import Bullet
import time
from Setting import *
from alien import *
from Setting_button import *

ai_setings = Setting()
Shoot = pygame.USEREVENT + 1

def check_keydown_events (event, ai_setings, stats, screen, play_button, setting_button, ship, aliens, bullet):
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        pygame.time.set_timer (Shoot, ai_setings.reload)
        pygame.event.get (Shoot)
    elif event.key == pygame.K_p:
        ai_setings.initialize_dynamic_settings ()
        stats.reset_stats()
        stats.game_active = True
        aliens.empty ()
        bullet.empty ()
        create_fleet (ai_setings, screen, ship, aliens)
        ship.center_ship()
        pygame.mouse.set_visible (False)



def check_keyup_events (event, ship, bullet):
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_s:
        ship.moving_down = False
    elif event.key == pygame.K_SPACE:
        pygame.time.set_timer (Shoot, ai_setings.stop_shooting)


def check_events(ai_setings, screen, stats, sb, play_button, setting_button, q_button, 
ship, aliens, bullet):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events (event, ai_setings, stats, screen, play_button, setting_button, ship, aliens, bullet)
        elif event.type == pygame.KEYUP:
            check_keyup_events (event, ship, bullet)
        elif event.type == Shoot:
            shooting (ai_setings, screen, ship, bullet)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setings, screen, stats, sb, play_button, ship,
                                    aliens, bullet, mouse_x, mouse_y)
            check_settings_button (ai_setings, screen, stats, sb, setting_button, ship,
                                    aliens, bullet, mouse_x, mouse_y)
            check_q_button (ai_setings, screen, stats, sb, q_button, ship,
                                    aliens, bullet, mouse_x, mouse_y)

def check_settings_button (ai_setings, screen, stats, sb, setting_button, ship,
                        aliens, bullet, mouse_x, mouse_y):
    s_button_clicked = setting_button.rect.collidepoint (mouse_x, mouse_y)
    if s_button_clicked and not stats.game_active:
        print ('settings')

def check_q_button (ai_setings, screen, stats, sb, q_button, ship,
                        aliens, bullet, mouse_x, mouse_y):
    q_button_clicked = q_button.rect.collidepoint (mouse_x, mouse_y)
    if q_button_clicked and  not stats.game_active:
        sys.exit()


def check_play_button (ai_setings, screen, stats, sb, play_button, ship,
                        aliens, bullet, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint (mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_setings.initialize_dynamic_settings ()
        stats.reset_stats()
        stats.game_active = True
        sb.perp_score ()
        sb.perp_high_score()
        sb.perp_level ()
        sb.perp_ship ()
        aliens.empty ()
        bullet.empty ()
        create_fleet (ai_setings, screen, ship, aliens)
        ship.center_ship()
        pygame.mouse.set_visible (False)

def get_number_rows (ai_setings, ship_height, alien_height):
    available_space_y = (ai_setings.screen_height - (3*alien_height) - ship_height)
    number_rows = int (available_space_y / (2*alien_height))
    return number_rows

def get_number_aliens_x(ai_setings, alien_width):
    available_space_x = ai_setings.screen_width - 2 * alien_width
    number_aliens_x = int (available_space_x/ (2*alien_width))
    return number_aliens_x

def create_alien (ai_setings, screen, aliens, alien_number, image, row_number):
    alien = Alien (ai_setings, screen, image)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width *alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
    aliens.add(alien)


def create_fleet (ai_setings, screen, ship, aliens):
    alien = Alien (ai_setings, screen, image)
    number_aliens_x = get_number_aliens_x (ai_setings, alien.rect.width)
    number_rows = get_number_rows (ai_setings, ship.rect.height,
        alien.rect.height)

    for row_number in range (number_rows):
        for alien_number in range (number_aliens_x):
            create_alien (ai_setings, screen, aliens, alien_number, image, row_number)



def update_screen(ai_setings, screen, stats, sb, ship, bullet, aliens, play_button, setting_button,
q_button):
    screen.fill (ai_setings.bg_color)
    for bullet in bullet.sprites():
        bullet.draw_bullet ()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score ()
    if not stats.game_active:
        play_button.draw_button()
        setting_button.draw_button ()
        q_button.draw_button ()
    pygame.display.flip()

def check_fleet_edges (ai_setings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction (ai_setings, aliens)
            break

def change_fleet_direction (ai_setings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setings.fleet_drop_speed
    ai_setings.fleet_direction *= -1

def update_aliens (ai_setings, stats, screen, sb, ship, aliens, bullet):
    check_fleet_edges (ai_setings, aliens)
    aliens.update ()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit (ai_setings, screen, stats, sb, ship, aliens, bullet)
    check_aliens_bottom (ai_setings, stats, screen, ship, aliens, bullet)

def ship_hit (ai_setings, screen, stats, sb, ship, aliens, bullet):
    if stats.ships_left > 0:
        stats.ships_left -=1
        aliens.empty ()
        bullet.empty ()
        create_fleet (ai_setings, screen, ship, aliens)
        ship.center_ship ()
        time.sleep(0.5)
        sb.perp_ship ()
    else:
        stats.game_active = False
        pygame.mouse.set_visible (True)


def update_bullet(ai_setings, screen, stats, sb, ship, bullet, aliens):
    bullet.update ()
    for bullets in bullet.copy():
        if bullets.rect.bottom <=0:
            bullet.remove (bullets)
    check_bullet_alien_collisions (ai_setings, screen, stats, sb, ship, aliens, bullet)



def check_bullet_alien_collisions (ai_setings, screen, stats, sb, ship, aliens, bullet):
    collisions = pygame.sprite.groupcollide (bullet, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_setings.alien_point * len(aliens)
        sb.perp_score ()
        check_high_score (stats, sb)

    if len (aliens) == 0:
        bullet.empty ()
        ai_setings.increase_speed ()
        stats.level +=1
        sb.perp_level()
        check_high_score (stats, sb)
        create_fleet (ai_setings, screen, ship, aliens)

def check_high_score (stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.perp_high_score ()

def check_aliens_bottom (ai_setings, stats, screen, ship, aliens, bullet):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit (ai_setings, screen, stats, sb, ship, aliens, bullet)
            break

def shooting (ai_setings, screen, ship, bullet):
    new_bullet = Bullet(ai_setings, screen, ship)
    bullet.add (new_bullet)
