import pygame
import Enemy
import Map
import Tower
import math
import TowerMenu
import TextDisplay
import WaveSystem

pygame.init()
window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
time = pygame.time.Clock()
menu = False
tiles = Map.Map(1920, 1080)

BasicEnemy = Enemy.Enemy("tile\\PNG\\Default size\\towerDefense_tile245.png", (840, 0))

j = pygame.image.load("tile\\PNG\\Default size\\towerDefense_tile245.png")
y = j.get_rect()
towerObj = Tower.Tower(j, y, "tile\\PNG\\Default size\\towerDefense_tile251.png")
tow = []
Menu = TowerMenu.TowerMenu(1920)
AllTowers = []
Alltowers2 = []
test = []

WaveObj = WaveSystem.WaveSystem()
Enemy_list = []
isWave = True

textEditor = TextDisplay.TextDisplay()
textEditor.change_text("Wave 1")
while True:
    dt = time.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if isWave:
            for i in range(WaveObj.calc_enemies(2)):
                Enemy_list.append(Enemy.Enemy("tile\\PNG\\Default size\\towerDefense_tile245.png", WaveObj.calc_enemies_starting_pos((840, -400), i)))
                isWave = False

        # The code that decides what you placed on the map and what to draw.
        if Menu.check:
            for i in range(len(Menu.towers_placed_list)):
                AllTowers.clear()
                Alltowers2.clear()
                AllTowers.append(Menu.towers_placed_list[i])
                Alltowers2.append(Menu.image_path_list[Menu.q.index(Menu.towers_placed_list[i])])
            for i in range(len(AllTowers)):
                tow.append(
                    Tower.Tower(Alltowers2[i], AllTowers[i], "tile\\PNG\\Default size\\towerDefense_tile251.png"))
            Menu.check = False

        test = Menu.towers_placed_list
        # Move sprites
        if event.type == pygame.KEYDOWN:
            if not menu:
                towerObj.place_indicator(event, tiles.getWalkTiles(), test)
            else:
                Menu.update_place_indicator(event)
            if event.key == pygame.K_m:
                menu = True
            if event.key == pygame.K_ESCAPE:
                menu = False

    # BasicEnemy.health = BasicTower.shoot(BasicEnemy.health)

    tiles.draw(window)
    BasicEnemy.move(window, dt)
    towerObj.draw_indicator(window)

    for i in tow:
        i.rotate_tower_to_enemy(i.calc_prediction(Enemy_list[len(Enemy_list) - 1].pos, BasicEnemy.speed))
        i.move_bullet()
        i.draw_bullet(window)
        if not menu:
            i.draw(window)
    for i in Enemy_list:
        i.move(window, dt)
    if menu:
        Menu.open_tower_menu(window)

    textEditor.draw_text(window)
    pygame.display.flip()

