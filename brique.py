import random

import pygame
from pygame.math import Vector2, Vector3


class Brique:
    def __init__(self, x, y):
        self.val = random.choice([0, 0, 3, 8, 12, 18])

        if 1 <= self.val < 5:
            color = Vector3(0, 255, 0)
        elif 5 <= self.val < 10:
            color = Vector3(255, 255, 0)
        elif 10 <= self.val < 15:
            color = Vector3(255, 125, 0)
        elif 15 <= self.val <= 20:
            color = Vector3(255, 0, 0)
        else:
            color = Vector3(0, 0, 0)

        self.couleur = color

        self.position = Vector2(x, y)

    def afficher(self, core):

        if 1 <= self.val < 5:
            color = Vector3(0, 255, 0)
        elif 5 <= self.val < 10:
            color = Vector3(255, 255, 0)
        elif 10 <= self.val < 15:
            color = Vector3(255, 125, 0)
        elif 15 <= self.val <= 20:
            color = Vector3(255, 0, 0)
        else:
            color = Vector3(0, 0, 0)

        self.couleur = color

        if self.val != 0:
            pygame.draw.rect(core.screen, self.couleur, (self.position.x, self.position.y, 35, 35))

