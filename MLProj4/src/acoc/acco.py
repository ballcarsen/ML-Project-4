#!/usr/bin/env python3

import random
from .cemetery_clustering import Cemetery
from .ant import Ant
import matplotlib.pyplot as plt
from pandas import DataFrame

class AntClustering():

    def __init__(self, ants, epochs, empty_cemetery,  neighborhood, data, max_move, alpha, sig):
        self.epochs = epochs
        self.max_move = max_move
        self.neighborhood = neighborhood
        self.cemetery = Cemetery(empty_cemetery, data)
        self.ants = []
        self.init_ants(ants, alpha, sig)

    def cluster(self):
        for epoch in range(self.epochs):
            print(epoch)
            for ant in self.ants:
                ant.move(self.neighborhood, self.max_move, self.cemetery)

    def init_ants(self, ants, alpha, sig):
        for a in range(ants):
            ant = Ant(self.cemetery.get_row(), self.cemetery.get_column(), alpha, sig)
            self.ants.append(ant)
            self.cemetery.insert_ant(ant)
    
    def print_cemetery(self):
        self.cemetery.dump()

    def output(self): # Print some crap - maybe throw out a plot or two
        #plt.ion()
        grid = self.cemetery.get_cemetery()
        x = []
        y = []
        for r in range(self.cemetery.get_row()):
            for c in range(self.cemetery.get_column()):
                if type(grid[r][c]) is Ant:
                    if grid[r][c].full_hand():
                        #print("Data", end=' ')
                        x.append(c)
                        y.append(r)
                    else: 
                        #print("None", end=' ')
                        pass
                elif grid[r][c]:
                    #print("Data", end=' ')
                    x.append(c)
                    y.append(r)
                else:
                    #print("None", end=' ')
                    pass
        #plt.pause(0.01)
        plt.clf()
        plt.scatter(x, y, s=1)
        plt.grid()
        plt.draw()
        plt.show(block=False)

    def show(self):
        plt.show()
