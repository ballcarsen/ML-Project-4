#!/usr/bin/env python3

'''
weights: |DATA| x # of clusters -> weights[i][j] = 1 if data[i] in cluster j, else 0
'''

class ACC():

    def __init__(self, ant_count = 50, clusters = 2, data, rho = 0.5):
        self.k = clusters
        self.data = data
        self.weights = []
        self.pheromones = []
        self.agents = []
        self.rho = rho
        self.clusters = [] # should be same length as data?
        self.init_weights()
        self.init_colony(ant_count)

    def cluster(self):
        pass

    def update_pheromones(self):
        for t in range(len(self.pheromones)):
            self.pheromones[t] = (1 - self.rho) * self.pheromones[t] + self.sum_pheromones()

    def sum_pheromones(self):
        pass

    def get_fitness(self, ant_count):
        sigma = 0
        for k in range(self.k):
            for n in range(len(self.data)):
                for m in range(len(self.data[n])):
                    sigma += self.weights * self.distance()

    def distance(self, vec_1, vec_2):

    # Randomly initialize the assigned cluster
    def init_colony(self):
        for d in range(len(self.data)):
            

    def select_cluster(self):
        pass

    def get_cluster_average(self):
        pass
