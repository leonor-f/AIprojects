import pygame

class Piece:
    def __init__(self, color, pos, image):
        self.color = color
        self.row = pos[0]
        self.col = pos[1]
        self.selected = False

    # def move(self, row, col):
