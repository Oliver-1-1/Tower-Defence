import pygame

class Enemy:

    def __init__(self, image_location, pos):
        self.image = pygame.image.load(image_location)
        self.pos = self.image.get_rect()
        self.pos.center = pos
        self.health = 100
        self.speed = 2

    def move(self, window):
        if not self.health <= 0:
            self.pos.move_ip(0, self.speed)
            window.blit(self.image, self.pos)


