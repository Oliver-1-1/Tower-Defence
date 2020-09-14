import pygame
import Enemy
import Map
import Tower
import math
import TowerMenu
import TextDisplay
import WaveSystem
import os
pygame.init()
window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
time = pygame.time.Clock()
menu = False
tiles = Map.Map(1920, 1080)

BasicEnemy = Enemy.Enemy("tile\\PNG\\Default size\\towerDefense_tile245.png", (840, 0))
o = pygame.image.load("tile\\PNG\\Default size\\towerDefense_tile203.png")
oo = o.get_rect()
BasicTower = Tower.Tower(o, oo, "tile\\PNG\\Default size\\towerDefense_tile251.png")

j = pygame.image.load("tile\\PNG\\Default size\\towerDefense_tile245.png")
y = j.get_rect()
towerObj = Tower.Tower(j, y, "tile\\PNG\\Default size\\towerDefense_tile251.png")
tow = []
Menu = TowerMenu.TowerMenu(1920)
AllTowers = []
Alltowers2 = []
isATowerPlaced = False


WaveObj = WaveSystem.WaveSystem()
Enemy_list = []
isWave = True

textEditor = TextDisplay.TextDisplay()

enemyDead = 0
RELOAD_SPEED = 2000

reloaded_event = pygame.USEREVENT + 1

reloaded = True
numOfEnemy = 0
wavenum = 0

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
            print("hi")
            numOfEnemy = WaveObj.calc_enemies(wavenum)
            Enemy_list.clear()
            for i in range(numOfEnemy):
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

    #Shoot
    if not isWave:
        if reloaded and isATowerPlaced:
            for towers in tow:
                if enemyDead == numOfEnemy:
                    wavenum += 1
                    Enemy_list.clear()
                    enemyDead = 0
                    numOfEnemy = WaveObj.calc_enemies(wavenum)
                    Menu.money += 300
                    for i in range(numOfEnemy):
                        Enemy_list.append(Enemy.Enemy("tile\\PNG\\Default size\\towerDefense_tile245.png", WaveObj.calc_enemies_starting_pos((840, -400), i)))
                if not Enemy_list[len(Enemy_list) - 1].dead:
                    Enemy_list[len(Enemy_list) - 1].health -= tow[0].shoot(20)
                    towers.test()
                    mm = towers.calc_prediction(Enemy_list[len(Enemy_list) - 1].pos, BasicEnemy.speed, dt)
                if Enemy_list[len(Enemy_list) - 1].health <= 0:
                    Enemy_list.pop(len(Enemy_list) - 1)
                    enemyDead += 1
            pygame.time.set_timer(reloaded_event, RELOAD_SPEED)
            reloaded = False



    for i in Enemy_list:
        if i.pos.centery > 1080:
            i.dead = True
            lives -= 1
            print("take")
    if lives <= 0:
        pygame.quit()
        print("hi")


    #draw
    tiles.draw(window)
    BasicEnemy.move(window, dt)
    towerObj.draw_indicator(window)
    BasicTower.draw(window)


    print(enemyDead, numOfEnemy)
    if enemyDead == numOfEnemy:
        isWave = True
        wavenum += 1
        enemyDead = 0
    if not isWave:
        for i in tow:
            i.rotate_tower_to_enemy(i.calc_angle(Enemy_list[len(Enemy_list) - 1].pos, BasicEnemy.speed))
            i.move_bullet(mm)
            i.draw_bullet(window)

            if not menu:
                i.draw(window)
        for i in Enemy_list:
            i.move(window, dt)
    if menu:
        Menu.open_tower_menu(window)

    textEditor.draw_text(window, (300,5))
    textEditor.change_text("Money: " + str(Menu.money))
    textEditor.draw_text(window, (1500, 5))
    pygame.display.update()


