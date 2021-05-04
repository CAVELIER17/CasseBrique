import pygame


class Accueil:
    def __init__(self, position, dimension, texte, couleur, longueur):
        self.position = position
        self.dimension = dimension
        self.texte = texte
        self.fontBB = pygame.font.Font('Police/AngelicWar.ttf', 70)
        self.textF = self.fontBB.render(self.texte, True, couleur)
        self.longueur = longueur

    def afficher(self, core):
        pygame.draw.rect(core.screen, (154, 153, 152), (self.position[0], self.position[1], self.dimension[0], self.dimension[1]))

        core.screen.blit(self.textF, (self.position[0]+(self.dimension[0]-self.longueur)/2, self.position[1]))

    def afficherfond(self):
        pass

    def BTNclic(self, position):
        if self.position[0] <= position[0] <= self.position[0]+self.dimension[0] and self.position[1] <= position[1] <= self.position[1]+self.dimension[1]:
            status = True
        else:
            status = False
        return status

    def Selection(self,Paccueil,Niveaux,posclic):
        for nv in Paccueil:
            if nv.BTNclic(posclic):
                difficulter = nv.texte
                print(difficulter)
        if difficulter == Niveaux[0]:
            scoreMax = 130
            acceleration = 1.014
        elif difficulter == Niveaux[1]:
            scoreMax = 175
            acceleration = 1.014
        elif difficulter == Niveaux[2]:
            scoreMax = 250
            acceleration = 1.014
        elif difficulter == Niveaux[3]:
            scoreMax = 500
            acceleration = 1.014
        return scoreMax,acceleration


