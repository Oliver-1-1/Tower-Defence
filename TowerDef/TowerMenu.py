import pygame


class TowerMenu:
    def __init__(self, screen_width):
        self.image = pygame.image.load("UI\\bricks.jpg").convert()
        self.image1 = pygame.image.load("UI\\Ui.png").convert()
        self.image_path_list = []
        self.image = pygame.transform.scale(self.image, (screen_width, 200))
        self.image1 = pygame.transform.scale(self.image1, (64, 64))

        self.rect = self.image.get_rect()
        self.rect1 = self.image1.get_rect()

        self.rect.centery, self.rect1.centery = 980, 1030
        self.rect1.centerx = screen_width / 2
        self.check = False

        # TileNumber that is usable in directory
        self.UsableTileList = [203, 204, 205, 206, 226, 227, 229, 245, 246, 247, 248, 249, 250, 251, 252, 291, 292, 268, 269]

        for imageNum in self.UsableTileList:
            self.image_path_list.append(
                pygame.image.load("tile\\PNG\\Default size\\towerDefense_tile" + str(imageNum) + ".png"))
        self.q = self.get_button_pos_list(self.image1)

        self.rect_indicator = pygame.Rect(128, 128, self.q[0].width, self.q[0].height)

        self.active = False
        self.index = None

        self.towers_placed_list = []

        self.money = 600

    def open_tower_menu(self, window):
        window.blit(self.image, self.rect)
        for i in range(len(self.q)):
            window.blit(self.image_path_list[i], self.q[i])

        pygame.draw.rect(window, (0, 0, 0), self.rect_indicator, 1)

    def update_place_indicator(self, event):
        if event.key == pygame.K_d:
            self.rect_indicator.move_ip(64, 0)
        if event.key == pygame.K_a:
            self.rect_indicator.move_ip(-64, 0)
        if event.key == pygame.K_w:
            self.rect_indicator.move_ip(0, -64)
        if event.key == pygame.K_s:
            self.rect_indicator.move_ip(0, 64)

        if event.key == pygame.K_RETURN and self.money >= 200:
            if self.active:
                self.towers_placed_list.append(self.q[self.index])
                self.rect_indicator = pygame.Rect(0, 0, self.q[0].width, self.q[0].height)
                self.active = False
                self.check = True
                self.money -= 200

            if not self.active:
                for index, i in enumerate(self.q):
                    if self.rect_indicator == i:
                        self.rect_indicator = self.q[index]
                        self.active = True
                        self.index = index

    @staticmethod
    def get_button_pos_list(image):
        buttonList = []

        for i in range(32, 1130, 128):
            rect = image.get_rect()
            rect.centery = 928
            rect.centerx = i
            buttonList.append(rect)

        for j in range(32, 1130, 128):
            rect = image.get_rect()
            rect.centery = 992
            rect.centerx = j
            buttonList.append(rect)

        return buttonList
