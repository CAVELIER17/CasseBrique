import pygame


class Rebond:
    def __init__(self):
        pass

    def RebondDG(self,bille,fen_x):
        if not bille.taille <= bille.position.x <= fen_x - bille.taille:
            bille.direction.x = -bille.direction.x

    def RebondHaut(self,bille):
        if (bille.position.y - bille.taille) <= 0:
            bille.direction.y = -bille.direction.y

    def RebondBrique(self,brique,bille,Zone,entraxeB,Score,val):
        if brique.position.x - Zone < bille.position.x < brique.position.x + entraxeB + Zone and brique.position.y - Zone < bille.position.y < brique.position.y + entraxeB + Zone:
            val = val - 1
            Score = Score + 1
            if brique.position.x - Zone < bille.position.x < brique.position.x + Zone / 2 or brique.position.x + entraxeB - Zone / 2 < bille.position.x < brique.position.x + entraxeB + Zone:
                bille.direction.x = -bille.direction.x

            if brique.position.y - Zone < bille.position.y < brique.position.y + Zone / 2 or brique.position.y + entraxeB - Zone / 2 < bille.position.y < brique.position.y + entraxeB + Zone:
                bille.direction.y = -bille.direction.y
        return Score,val

    def RebondTable(self,player,bille,fen_y):
        if (fen_y - (player.taille / 2) - player.hauteurplayer) <= (bille.position.y + bille.taille) <= (fen_y + (
                player.taille / 2) - player.hauteurplayer) and player.position.x - player.largeur <= bille.position.x <= player.position.x + player.largeur:
            if player.position.x - player.largeur <= bille.position.x <= player.position.x - player.largeur + 20 or player.position.x + player.largeur - 20 <= bille.position.x <= player.position.x + player.largeur:
                posx = bille.direction.x
                bille.direction.x = -bille.direction.y
                bille.direction.y = posx
            else:
                bille.direction.y = -bille.direction.y