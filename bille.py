import random

import pygame
from pygame.math import Vector2, Vector3


class Bille:
    def __init__(self):
        self.taille = 6
        self.direction = Vector2(0, 0)
        self.position = Vector2(0, 0)
        self.couleur = Vector3(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.start = False

    def deplacer(self, position):
        self.position = Vector2(position)



    def afficher(self, core):
        pygame.draw.circle(core.screen, self.couleur, self.position, self.taille)
