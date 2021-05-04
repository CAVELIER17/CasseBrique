import time

import pygame
from pygame.constants import K_BREAK, K_q

from Page.accueil import Accueil
from Page.perdu import Perdu
from Page.gagne import Gagne
from Page.pause import Pause
from rebond import Rebond
from p5 import core
from player import Player
from brique import Brique
from bille import Bille


# Initialisation Variable
Niveaux = ["Facile", "Intermediaire", "Difficile", "Expert"]
LongueurTXT = [4*35,9*35,6*35,5*35]
Paccueil = []
briques = []
player1 = None
bille1 = None
RBD = None
fen_x = 770
fen_y = 800
dimBTN = (500,90)
entraxeB = 35
demarrage = False
fin = False
pause = False
Score =  0
Zone = 2
tempscore = 0
scoreMax = 100
acceleration = 1.014

def setup():

    # Initialisation fenetre
    core.fps = 120*2
    core.WINDOW_SIZE = [fen_x, fen_y]
    core.TITLE_WINDOW = "Casse Brique"

    # Initialisation Variable
    global player1, Findelapartie, bille1, Gagner,fontW, pauseT, LongueurTXT, RBD
    Findelapartie = Perdu()
    Gagner = Gagne()
    pauseT = Pause()
    RBD = Rebond()
    fontW = pygame.font.Font('Police/WEST.TTF', 30)

    # Création player, bille, briques
    player1 = Player((fen_x, fen_y))
    bille1 = Bille()
    for i in range(0, 22):
        for j in range(0, 1):
            briques.append(Brique(i * entraxeB, j * entraxeB))

    nb = 0
    for NV in Niveaux:
        posNv = ((fen_x - dimBTN[0]) / 2, 120 + dimBTN[1] * 2 * nb)
        Paccueil.append(Accueil(posNv, dimBTN, NV, (255, 255, 255),LongueurTXT[nb]))
        nb += 1


def run():
    global demarrage, fin, pause, Score, Findelapartie, tempscore, Gagner, pause, RBD, scoreMax, acceleration
    frontMT = False

    for b in briques:
        b.afficher(core)

    # Affichage Score
    ScoreT = fontW.render("Score : " + str(Score), True, (255, 255, 255))
    core.screen.blit(ScoreT, (35, fen_y-30))

    if fin:
        demarrage = False
        if len(briques) != 0:
            Findelapartie.afficher((fen_x, fen_y))
        else:
            Gagner.afficher((fen_x, fen_y))

        if core.getMouseLeftClick():
            fin = False
    else:
        if demarrage:

            player1.afficher(core)
            bille1.afficher(core)

            bille1.deplacer((bille1.position.x - bille1.direction.x, bille1.position.y + bille1.direction.y))

            if Score % 5 == 0 and Score != tempscore and Score < scoreMax:
                tempscore = Score
                bille1.direction.x = bille1.direction.x * acceleration
                bille1.direction.y = bille1.direction.y * acceleration


            # Mode Pause
            pause = pauseT.ModePause(pause,player1,bille1,(fen_x,fen_y))

            # Gestion des briques
            for t in briques:
                if t.val <= 0:
                    briques.remove(t)
                Score,t.val = RBD.RebondBrique(t,bille1,Zone,entraxeB,Score,t.val)

            # Rebond droite/gauche
            RBD.RebondDG(bille1,fen_x)

            # Rebond plafond
            RBD.RebondHaut(bille1)

            # Rebond table
            RBD.RebondTable(player1,bille1,fen_y)

            # Bille perdu
            if bille1.position.y >= fen_y - player1.hauteurplayer + 20:
                fin = True

            if len(briques) == 0:
                fin = True


        else:

            bille1.deplacer((fen_x / 2, fen_y - player1.hauteurplayer - (player1.taille / 2) - bille1.taille))
            player1.deplacer((fen_x / 2, 0))
            player1.afficher(core)
            bille1.afficher(core)


            for BTN in Paccueil:
                BTN.afficher(core)

            if core.getMouseLeftClick():
                posclic = core.getMouseLeftClick()
                scoreMax,acceleration = Paccueil[0].Selection(Paccueil,Niveaux,posclic)
                bille1.direction.x = 1/2
                bille1.direction.y = -1.5/2
                Score = 0
                demarrage = True


if __name__ == '__main__':
    core.main(setup, run)