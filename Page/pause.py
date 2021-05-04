import pygame
from pygame.constants import K_p

from p5 import core


class Pause:
    def __init__(self):
        self.font = pygame.font.Font('Police/Break.ttf', 150)
        self.fronMTPause = None

    def afficher(self, fenetre):
        self.pause = self.font.render("Pause", True, (243, 201, 13))
        core.screen.blit(self.pause, ((fenetre[0]-455)/2, (fenetre[1]-150)/2))

    def ModePause(self,pause,player,bille,fen):
        if pygame.key.get_pressed()[K_p] and not self.fronMTPause or not pygame.key.get_pressed()[K_p] and self.fronMTPause:
            if pygame.key.get_pressed()[K_p] and not self.fronMTPause:
                pause = not pause
            self.fronMTPause = not self.fronMTPause

        if pause:
            player.deplacer((bille.position.x, 0))
            self.afficher(fen)
        else:
            player.deplacer(pygame.mouse.get_pos())
        return pause