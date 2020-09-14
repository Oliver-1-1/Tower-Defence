class WaveSystem:

    def __init__(self):
        self.enemy_starting_number = 5
        self.enemy_adding_factor = 2.5
        self.enemy_distancing_number = 70  # Should be given in pixels
        self.waveNum = 0
    def calc_enemies(self, wave_number):
        self.waveNum = wave_number
        return self.enemy_starting_number + int(wave_number * self.enemy_adding_factor)

    def calc_enemies_starting_pos(self, starting_coordinate, num):
        return starting_coordinate[0], num * self.enemy_distancing_number + starting_coordinate[1]

