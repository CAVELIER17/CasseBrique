import pygame

from p5 import core


class Gagne:
    def __init__(self):
        self.fontBB = pygame.font.Font('Police/AngelicWar.ttf', 150)

    def afficher(self, fenetre):
        self.Youwin = self.fontBB.render("you win", True, (243, 201, 13))
        core.screen.blit(self.Youwin, ((fenetre[0]-455)/2, (fenetre[1]-150)/2))
