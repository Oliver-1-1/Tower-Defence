import pygame
import Enemy
import Map
import Tower
import math
import TowerMenu
import TextDisplay
import WaveSystem
import os
import py2exe
pygame.init()
window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
time = pygame.time.Clock()

image = pygame.image.load("tile\\PNG\\Default size\\towerDefense_tile203.png")
rect = image.get_rect()

menu = False
isATowerPlaced = False
isWave = True
reloaded = True


tiles = Map.Map(1920, 1080)
Menu = TowerMenu.TowerMenu(1920)
textEditor = TextDisplay.TextDisplay()
WaveObj = WaveSystem.WaveSystem()
towerObj = Tower.Tower(image, rect, "tile\\PNG\\Default size\\towerDefense_tile251.png")


# these are for creating the towers with right texture and rect. They have bad names
AllTowers = []
Alltowers2 = []
tow = []

Enemy_list = []


enemyDead = 0
RELOAD_SPEED = 2000
numOfEnemy = 0
wavenum = 0

reloaded_event = pygame.USEREVENT + 1


lives = 3
while True:
    dt = time.tick(60)
    textEditor.change_text("Wave: " + str(WaveObj.waveNum))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == reloaded_event:
            reloaded = True
            qq = True
            pygame.time.set_timer(reloaded_event, 0)

        if isWave:

            numOfEnemy = WaveObj.calc_enemies(wavenum)
            Enemy_list.clear()
            for i in range(numOfEnemy):
                Enemy_list.append(Enemy.Enemy("tile\\PNG\\Default size\\towerDefense_tile245.png",
                                              WaveObj.calc_enemies_starting_pos((840, -400), i)))
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
                isATowerPlaced = True
            Menu.check = False

        # Move sprites
        if event.type == pygame.KEYDOWN:
            if not menu:
                towerObj.place_indicator(event, tiles.getWalkTiles(), Menu.towers_placed_list)
            else:
                Menu.update_place_indicator(event)
            if event.key == pygame.K_m:
                menu = True
            if event.key == pygame.K_ESCAPE:
                menu = False

    # Shoot

    if reloaded and isATowerPlaced:
        for towers in tow:
            # Start new wav
            if enemyDead == numOfEnemy:
                wavenum += 1
                Enemy_list.clear()
                enemyDead = 0
                numOfEnemy = WaveObj.calc_enemies(wavenum)
                Menu.money += 300
                for i in range(numOfEnemy):
                    Enemy_list.append(Enemy.Enemy("tile\\PNG\\Default size\\towerDefense_tile245.png",
                                                  WaveObj.calc_enemies_starting_pos((840, -400), i)))

            # Shoot enemy and take away health and remove from Enemt_list
            if not Enemy_list[len(Enemy_list) - 1].dead:
                Enemy_list[len(Enemy_list) - 1].health -= tow[0].shoot(20)
                towers.test()
                mm = towers.calc_prediction(Enemy_list[len(Enemy_list) - 1].pos, Enemy_list[0].speed, dt)
            if Enemy_list[len(Enemy_list) - 1].health <= 0:
                Enemy_list.pop(len(Enemy_list) - 1)
                enemyDead += 1
        pygame.time.set_timer(reloaded_event, RELOAD_SPEED)
        reloaded = False

    # Check if enemy is dead
    for i in Enemy_list:
        if i.pos.centery > 1080:
            i.dead = True
            lives -= 1
            print("take")
    if lives <= 0:
        pygame.quit()
        print("hi")

    # draw
    tiles.draw(window)
    towerObj.draw_indicator(window)
    for i in Enemy_list:
        i.move(window, dt)

    # Rotate tower, and move bullet
    for i in tow:
        i.rotate_tower_to_enemy(i.calc_angle(Enemy_list[len(Enemy_list) - 1].pos, Enemy_list[0].speed))
        i.move_bullet(mm)
        i.draw_bullet(window)
        if not menu:
            i.draw(window)

    if menu:
        Menu.open_tower_menu(window)

    # Text
    textEditor.draw_text(window, (300, 5))
    textEditor.change_text("Money: " + str(Menu.money))
    textEditor.draw_text(window, (1500, 5))

    pygame.display.update()
