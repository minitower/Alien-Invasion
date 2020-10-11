class Setting ():
    def __init__(self):
        self.screen_width = 1900
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_collor = 60, 60, 60
        self.bullet_allowed = 3
        self.reload = 250
        self.stop_shooting = self.reload + 999999999
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 3
