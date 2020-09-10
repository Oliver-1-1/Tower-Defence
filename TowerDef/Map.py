import pygame

tileString = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxuuuuuu" \
             "uuuuuuuuuuuyyyyyyyyyyyyyyyyyxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
             "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \



tileMap = []
tileLayout = []
tileImages = []
walkTiles = []


class Map:
    def __init__(self, screen_width, screen_height):
        tileImages.append(pygame.image.load("tile\\PNG\\Default size\\towerDefense_tile230.png").convert())
        tileImages.append(pygame.image.load("tile\\PNG\\Default size\\towerDefense_tile231.png").convert())
        tileImages.append(pygame.image.load("tile\\PNG\\Default size\\towerDefense_tile232.png").convert())
        tileImages.append(pygame.image.load("tile\\PNG\\Default size\\towerDefense_tile291.png").convert())

        for i in range(int(screen_width / 64) + 1):
            for j in range(int(screen_height / 64) + 1):
                tileMap.append(pygame.Rect(i * 64, j * 64, 64, 64))

    @staticmethod
    def draw(window):
        for i in range(len(tileString)):
            if tileString[i] == 'x':
                window.blit(tileImages[1], tileMap[i])
            if tileString[i] == 'y':
                window.blit(tileImages[0], tileMap[i])
                walkTiles.append(tileMap[i].center)
            if tileString[i] == 'u':
                window.blit(tileImages[2], tileMap[i])
                walkTiles.append(tileMap[i].center)
                

    @staticmethod
    def getWalkTiles():
        return walkTiles
