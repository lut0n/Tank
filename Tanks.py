import pygame
import random
import time
import keyboard
import Tank
 
pygame.init()
X = 900
Y = 800

screen = pygame.display.set_mode((X, Y))
 
pygame.display.set_caption('TANKS')
status = True

tank_1 = Tank.Tank(screen, 'red_tank.png', ['w', 's', 'a', 'd'])
tank_2 = Tank.Tank(screen, 'blue_tank.png', ['i', 'k', 'j', 'l'])
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
        tank_1.show()
        tank_1.update()
        tank_2.show()
        tank_2.update()
        pygame.display.flip()
        screen.fill((0,0,0))
pygame.quit()


