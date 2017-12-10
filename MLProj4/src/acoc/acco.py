#!/usr/bin/env python3

import random
from cemetery_clustering import Cemetery


class AntClustering():

    def __init__(self, ants=50, epochs=1000, empty_cemetery,  neighborhood, data, max_move):
        self.epochs = epochs
        self.max_move = max_move
        self.neighborhood = neighborhood
        self.cemetery = Cemetery(empty_cemetery, data)
        self.ants = self.init_ants(ants)

    def cluster(self):
        for epoch in range(self.epochs):
            for ant in self.ants:
                ant.move(self.neighborhood, self.max_move, cemetery)

    def init_ants(self, ants):
        for a in range(ants):
            ant = Ant(self.cemetery.get_row(), self.cemetery.get_column())
            self.ants.append(ant)
            self.cemetery.insert_random_location(ant)

    def output(self): # Print some crap - maybe throw out a plot or two
        pass

