import random
import pygame
import keyboard

class Tank():
    def __init__(self, screen, image_name, control):
        self.alive = True
        self.up = control[0]
        self.down = control[1]
        self.left = control[2]
        self.right = control[3]
        self.image = pygame.image.load(image_name)
        self.screen = screen
        self.image_default = self.image
        self.direction = [0,0,0,0]
        while True:
            self.x = random.randint(0,860)
            if self.x % 10 == 0:
                break
        while True:
            self.y = random.randint(0,760)
            if self.y % 10 == 0:
                break

    def update(self):
        if self.alive:
            key = pygame.key.get_pressed()
            if keyboard.is_pressed(self.up):
                self.y -= 10
                if self.y < 0:
                    self.y = 0
                self.direction = [1,0,0,0]
            elif keyboard.is_pressed(self.down):
                self.y += 10
                if self.y >760:
                    self.y=760
                self.direction = [0,1,0,0]
            elif keyboard.is_pressed(self.left):
                self.x -= 10
                if self.x < 0:
                    self.x = 0
                self.direction = [0,0,1,0]
            elif keyboard.is_pressed(self.right):
                self.x += 10
                if self.x >860:
                    self.x=860
                self.direction = [0,0,0,1]
            if self.direction == [1,0,0,0] :
                self.image = self.image_default
            elif self.direction == [0,1,0,0]:
                self.image = pygame.transform.rotate(self.image_default, 180)
            elif self.direction == [0,0,0,1]:
                self.image = pygame.transform.rotate(self.image_default, 270)
            elif self.direction == [0,0,1,0]:
                self.image = pygame.transform.rotate(self.image_default, 90)
    def show(self):
        self.screen.blit(self.image, (self.x, self.y))
    def show(self):
        self.screen.blit(self.image, (self.x, self.y))
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
