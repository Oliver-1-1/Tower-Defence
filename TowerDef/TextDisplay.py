import pygame

class TextDisplay:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('INVASION2000.TTF', 60)
        self.text = None

    def change_text(self, text):
        self.text = self.font.render(text, False, (0,0,0))

    def draw_text(self, window):
        window.blit(self.text, (300, 5))