import pygame

class Enemy:
    def __init__(self, image_location, pos):
        self.image = pygame.image.load(image_location)
        self.pos = self.image.get_rect()
        self.pos.center = pos
        self.health = 100
        self.speed = 0.1
        self.dead = False

    def move(self, window, dt):
        if not self.health <= 0 and not self.dead:
            self.pos.move_ip(0, self.speed * dt)
            window.blit(self.image, self.pos)
        if self.dead:
            self.pos.center = (500, -20)



