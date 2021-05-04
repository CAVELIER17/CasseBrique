import random

import pygame
from pygame import Vector2


class Drop:
    def __init__(self, largeur):
        self.gravity = random.randint(1, 10)
        self.size = random.randint(1, 20)
        self.R = random.randint(0, 255)
        self.V = random.randint(0, 255)
        self.B = random.randint(0, 255)
        self.position = Vector2(random.randint(0, largeur),  random.randint(-largeur, 0))

    def tomber(self, hauteur):
        self.position.y = self.position.y+self.gravity
        if self.position.y > hauteur:
            self.raz()

    def raz(self):
        self.position.y = 0

    def afficher(self, core):
        pygame.draw.line(core.screen, (self.R, self.V, self.B), (self.position.x, self.position.y), (self.position.x, self.position.y + self.size), 1)