#!/usr/bin/env python3

import random
import math

class Cemetery():

    def __init__(self, space, data):
        self.cemetery = []
        self.init_space(space, len(data))
        self.populate_cemetery(data)

    def init_space(self, space, length):
        dimension = math.ceil(space * length) / 4)
        for row in range(dimension):
            row = []
            for column in range(dimension):
                row.append(None)
            self.cemetery.append(row)

    def populate_cemetery(self, data):
        inserted = 0
        for row in range(len(self.cemetery)):
            for column in range(len(self.cemetery[row])):
                if random.random() > 0.5:
                    self.set_grave(row, column, data[inserted])
                    inserted += 1
        if inserted < len(data):
            pass # Not all data points got inserted... probably need to handle this

    def get_column(self): # Return cemetery width
        return len(self.cemetery)

    def get_row(self): # Return cemetery height
        return len(self.cemetery[0])

    def set_grave(self, row, column, instance = None): # update grave
        if not instance:
            self.cemetery[row][column] = None
        else:
            self.cemetery[row][column] = instance

    def get_grave(self, row, column): # Return whatever is six feet deep
        return self.cemetery[row][column]

    def insert_random_location(self, ant): # used for movement and/or ant location initialization
        self.set_grave(random.randint(0, self.get_row - 1), random.randint(0, self.get_column - 1), ant)
