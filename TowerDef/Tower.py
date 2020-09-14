import pygame

import math


class Tower:

    def __init__(self, image, rect, image_bullet_location):
        self.image = image
        self.pos = rect
        self.original_image = self.image
        self.original_pos = self.pos
        self.active = False
        self.index = -1

        self.image_bullet = pygame.image.load(image_bullet_location)
        self.pos_bullet = self.image_bullet.get_rect()
        self.bullet_speed = 0.5

        self.image_bullet_explosion = pygame.image.load("flame.png")
        self.pos_bullet_explosion = self.image_bullet_explosion.get_rect()
        self.one = False

    def place_indicator(self, event, blocked_tiles, all_towers):
        if event.key == pygame.K_d:
            self.pos.move_ip(64, 0)
        if event.key == pygame.K_a:
            self.pos.move_ip(-64, 0)
        if event.key == pygame.K_w:
            self.pos.move_ip(0, -64)
        if event.key == pygame.K_s:
            self.pos.move_ip(0, 64)

        if event.key == pygame.K_b:
            for index, i in enumerate(all_towers):
                if self.pos.centerx == i.centerx and self.pos.centery == i.centery:
                    self.index = index
                    self.active = True

        if self.active:
            if event.key == pygame.K_RETURN:
                mySet = set(blocked_tiles)
                if not (self.pos.centerx, self.pos.centery) in mySet:
                    all_towers[self.index].clamp_ip(self.pos)
                    self.index = 0
                    self.active = False

    def shoot(self, health):
        self.pos_bullet.move_ip(2, 2)
        health -= 0
        return health

    def draw_indicator(self, window):
        pygame.draw.rect(window, (0, 0, 0), self.pos, 1)

    def draw(self, window):
        window.blit(self.image, self.pos)
        window.blit(self.image_bullet, self.pos_bullet)

    def calc_angle(self, enemy_pos, towerPos):
        a, b = enemy_pos.centerx - self.pos.centerx, \
               enemy_pos.centery - self.pos.centery
        angle = math.degrees(-math.atan2(b, a))

        return angle - 90

    def rotate_tower_to_enemy(self, angle):
        self.image = pygame.transform.rotate(self.original_image, angle)

    def calc_prediction(self, enemy_pos, enemy_speed, dt):
        a, b = enemy_pos.centerx - self.pos.centerx, \
               enemy_pos.centery - self.pos.centery


        timeA = a / 2000 * dt
        timeB = b / 2000 * dt
        return timeA, timeB


    def move_bullet(self, speed):
        self.pos_bullet.move_ip(speed[0], speed[1])

    def test(self):
        self.pos_bullet.center = self.pos.center

    def draw_bullet(self, window):
        window.blit(self.image_bullet, self.pos_bullet)

    def draw_explosion(self, window, enemy_pos):
        if not self.one:
            self.pos_bullet_explosion.center = enemy_pos
            self.one = True
        window.blit(self.image_bullet_explosion, self.pos_bullet_explosion)

