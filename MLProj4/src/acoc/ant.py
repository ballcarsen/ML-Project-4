#!/usr/bin/env python3

import random
import math

class Ant():

    def __init__(self, row, column, alpha, sig):
        self.row = random.randint(0, row - 1)
        self.column = random.randint(0, column - 1)
        self.hand = None
        self.sig = sig # Tune
        self.alpha = alpha # Tune
        self.k1 = 1 # Tune
        self.k2 = 1 # Tune

    def move(self, neighborhood, max_move, cemetery): # generate a new random point (within a threshold) and move there
        placed = False
        while not placed:
            column = random.randint(-max_move, max_move) + self.column
            row = random.randint(-max_move, max_move) + self.row
            if row >= len(cemetery.get_row()) or column >= len(cemetery.get_column()) or column == 0 or row == 0: # if not a good move, redo
                continue
            self.row = row
            self.column = column
            if self.full_hand and not cemetery[self.row][self.column]:
                self.drop(cemetery, neighborhood)
            elif not self.full_hand and cemetery[self.row][self.column]:
                self.pick_up(cemetery, neighborhood)
            placed = True


    def get_neighbors(self, row, column, cemetery, neighborhood):
        neighbors = []
        for r, c in [(row + i, column + j) for i in range(-neighborhood, neighborhood + 1) for j in range(-neighborhood, neighborhood + 1) if i != 0 or j != 0]:
            if r >= len(cemetery.get_row()) or c >= len(cemetery.get_column()): # can't add because I am at the border
                neighbors.append(cemetery.get_grave(r, c))
        return neighbors 

    def pick_up(self, cemetery, neighborhood):
        probability = (self.k1 / (self.k1 + self.calc_similarity(self.row, self.column, cemetery, neighborhood)))**2
        if probability > 0.5:
            self.hand = cemetery.get_grave(self.row, self.column)

    def drop(self, cemetery, neighborhood):
        similarity = self.calc_similarity(self.row, self.column, cemetery, neighborhood)
        probability = (similarity / (self.k2 + similarity))**2
        if probability > 0.5:
            cemetery.set_grave(self.row, self.column, self.hand)
            self.hand = None

    def calc_similarity(self, row, column, cemetery, neighborhood):
        neighbors = self.get_neighbors(row, column, cemetery, neighborhood)
        sigma = 0
        current = cemetery.get_grave(row, column)
        for n in neighbors:
            sigma += (1 - (self.get_distance(current, n) / self.alpha))
        f = (1 / self.sig**2) * sigma
        if f < 0:
            f = 0
        return f

    def distance(self, current, neighbor):
        sigma = 0
        for i in range(len(current)):
            sigma += (current[i] - neighbor[i])**2
        return math.sqrt(sigma)

    def full_hand(self):
        if not self.hand:
            return False
        return True
