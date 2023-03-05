import pygame
from dino_runner.utils.constants import RUNNING
from dino_runner.utils.constants import DUCKING
from dino_runner.utils.constants import JUMPING
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    Y_POST = 310
    X_POST = 80
    jump_count = 10

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POST
        self.dino_rect.y = self.Y_POST
        self.step = 0


    def update(self, user_input):
        if user_input[pygame.K_DOWN]:
            self.duck()
        elif user_input[pygame.K_UP]:
            self.jump()
        else:
            self.run()
            self.Y_POST = 310
            self.jump_count = 10

        self.step += 1
        if self.step == 10:
            self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUNNING[0] if self.step < 5 else  RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POST
        self.dino_rect.y = self.Y_POST

    def duck(self):
        self.image = DUCKING[0] if self.step < 5 else  DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POST
        self.dino_rect.y = self.Y_POST + 35
    
    
    def jump(self):
        self.image = JUMPING
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POST
        self.dino_rect.y = self.Y_POST

        if self.jump_count >= -10:
            print(self.dino_rect.y, '=', self.dino_rect.y, '- (', self.jump_count, '*', abs(self.jump_count), ') * 0.5' )
            self.Y_POST -= (self.jump_count * abs(self.jump_count)) * 0.5
            self.jump_count -= 1
        else:
            self.jump_count = 10



