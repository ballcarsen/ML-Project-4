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
        #cemetery.dump()
        while not placed:
            print("Self", self.row, self.column)
            column = random.randint(-max_move, max_move)
            row = random.randint(-max_move, max_move)
            if (column == 0 and row == 0): # if not a good move, redo
                print("Move", row, column)
                #cemetery.dump()
                continue
            temp_row = self.row + row
            temp_col = self.column + column
            if temp_row < 0 or temp_col < 0 or temp_col >= cemetery.get_column() or temp_row >= cemetery.get_row():
                print("Move", row, column)
                #cemetery.dump()
                continue
            if type(cemetery.get_grave(temp_row, temp_col)) is Ant:
                continue
            print("Move", row, column)
            cemetery.set_grave(self.row, self.column, None)
            self.row = temp_row
            self.column = temp_col
            #print("Column: %s, Row: %s\nCem_col: %s, Cem_row: %s" % (column, row, cemetery.get_column(), cemetery.get_row()))
            #print(self.full_hand())
            if self.full_hand() and not cemetery.get_grave(self.row, self.column):
                self.drop(cemetery, neighborhood)
            elif not self.full_hand() and cemetery.get_grave(self.row, self.column):
                self.pick_up(cemetery, neighborhood)
            placed = True


    def get_neighbors(self, row, column, cemetery, neighborhood):
        neighbors = []
        for r, c in [(row + i, column + j) for i in range(-neighborhood, neighborhood + 1) for j in range(-neighborhood, neighborhood + 1) if i != 0 or j != 0]:
            if r < cemetery.get_row() and c < cemetery.get_column() and r >= 0 and c >= 0: # can't add because I am at the border
                neighbor = cemetery.get_grave(r, c)
                if neighbor and type(neighbor) is not Ant:
                    neighbors.append(cemetery.get_grave(r, c))
        return neighbors 

    def pick_up(self, cemetery, neighborhood):
        probability = (self.k1 / (self.k1 + self.calc_similarity(self.row, self.column, cemetery, neighborhood)))**2
        if probability > 0.5:
            self.hand = cemetery.get_grave(self.row, self.column)
            print("POINT PICKED UP")

    def drop(self, cemetery, neighborhood):
        similarity = self.calc_similarity(self.row, self.column, cemetery, neighborhood)
        probability = (similarity / (self.k2 + similarity))**2
        if probability > 0.5:
            cemetery.set_grave(self.row, self.column, self.hand)
            self.hand = None
            print("POINT DROPPED")

    def calc_similarity(self, row, column, cemetery, neighborhood):
        #print("Start of get_neighbors")
        neighbors = self.get_neighbors(row, column, cemetery, neighborhood)
        #print("End of get_neighbors")
        sigma = 0
        if self.full_hand():
            current = self.hand
        else:
            current = cemetery.get_grave(row, column)
        for n in neighbors:
            sigma += (1 - (self.get_distance(current, n) / self.alpha))
        f = (1 / self.sig**2) * sigma
        if f < 0:
            f = 0
        return f

    def get_distance(self, current, neighbor):
        sigma = 0
        for i in range(len(current)):
            sigma += (int(current[i]) - int(neighbor[i]))**2
        return math.sqrt(sigma)

    def full_hand(self):
        if not self.hand:
            return False
        return True

    def force_pick_up(self, data):
        self.hand = data

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def set_row(self, row):
        self.row = row

    def set_column(self, col):
        self.column = col

    def get_hand(self):
        return self.hand
