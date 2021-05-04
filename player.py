import random

import pygame
from pygame.math import Vector2, Vector3


class Player:
    def __init__(self, fenetre):
        self.taille = 8
        self.fenetre = fenetre
        self.largeur = 40
        self.direction = Vector2(-5, -5)
        self.position = Vector2(fenetre[0]/2, fenetre[1])
        self.hauteurplayer = 50
        self.couleur = Vector3(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def deplacer(self, position):
        self.position.x = position[0]
        self.position.y = position[1]

    def afficher(self, core):
        pygame.draw.line(core.screen, self.couleur, (self.position.x-self.largeur, self.fenetre[1]-self.hauteurplayer), (self.position.x+self.largeur, self.fenetre[1] -self.hauteurplayer), self.taille)
