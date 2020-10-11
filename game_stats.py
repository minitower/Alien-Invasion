class GameStats ():

    def __init__ (self, ai_setings):
        self.ai_setings = ai_setings
        self.reset_stats()
        self.game_active = False

    def reset_stats (self):
        self.ships_left = self.ai_setings.ship_limit
