"""
max cols = 22
max rows = 11
min gap  = 5
"""

class Settings():

    def __init__(self):
        
        #game settings
        self.game_active = True
        #num of cols, num of rows, space btw aliens,
        self.wave_spec = [[ 8,  5, 36],
                          [ 8,  6, 25],
                          [12,  7, 20],
                          [16,  7, 10],
                          [18,  8,  5]]
        self.wave = 0
        self.wave_counter = 0
        self.wave_max = len(self.wave_spec) - 1
            
        #screen settings
        self.screen_dim = (840, 600)
        self.screen_gap = 30
        self.screen_height = self.screen_dim[1] - (3 * self.screen_gap)
        self.screen_path = 'images/background.bmp'
        
        #player settings
        self.player_width = 30
        self.player_start_pos = (420, 570)
        self.player_speed_factor = 2
        self.player_max_hp = 2
        self.player_hp = self.player_max_hp

        #bullet settings
        self.bullet_speed = 4
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 77, 77)

        #alien settings
        self.alien_width = 30
        self.alien_x_speed = 1
        self.alien_y_speed = 10
        self.alien_direction = 1

        #hp settings
        self.hearth_x = self.screen_dim[0] - self.screen_gap
        self.hearth_y = self.screen_dim[1] - 28
