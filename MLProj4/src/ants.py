#!/usr/bin/env python3

import random
import math
import numpy as np

class ACC():

    def __init__(self, ant_count, k, data, rho, qnot):
        self.k = k
        self.q0 = qnot
        self.clusters = [] # Need to initialize somewhere
        self.data = data
        self.weights = []
        self.pheromones = [] # data point x cluster
        self.agents = [] # Array of solution strings
        self.rho = rho
        self.init_weights()
        self.init_colony(ant_count)
        self.init_pheromones()
        self.calc_cluster_average()

        def cluster(self):
            pass

        def init_weights(self):
            for n in range(len(self.data)):
                cluster_vector = []
                for k in range(self.k):
                    cluster_vector.append(0)
                index = random.randint(0, self.k - 1)
                cluster_vector[index] = 1 # randomly assign cluster initially
                self.weights.append(cluster_vector)

        def init_pheromones(self):
            for i in range(len(self.data)):
                pharaoh = []
                for j in range(self.k):
                    pharaoh.append(random.uniform(0.01, 0.3))
                self.pheromones.append(pharaoh)

        def init_colony(self, ants):
            for a in range(ants):
                solution_string = []
                for n in range(len(self.data)):
                    solution_string.append(random.randint(0, self.k - 1))
                self.agents.append(solution_string)

        def distance(self, vec_1, vec_2): # Euclidean distance squared
            sigma = 0
            for i in range(len(vec_1)): # assuming equal length
                sigma += (vec_1[i] - vec_2[i])**2
            return sigma

        def update_pheromones(self):
            fittest = self.get_most_fit()
            for i in range(len(self.data)):
                for j in range(len(self.k)):
                    delta_tao = 

        def generate_solutions(self):
            # Clear old solutions
            for a in range(len(self.agents)):
                self.agents[a] = []
            for i in range(len(self.data)):
                sigma = 0
                distribution = []
                choices = []
                for j in range(len(self.k)):
                    sigma += self.pheromones[i][j]
                for j in range(len(self.k)):
                    distribution.append(self.pheromones[i][j] / sigma)
                    choices.append(j)
                for a in self.agents:
                    a.append(np.random.choice(choices, None, p=distribution))
                    

        def calc_cluster_average(self):
            for j in range(self.k):
                weight_sum = 0
                for i in range(len(self.data)):
                    weight_element_sum = 0
                    for v in range(len(self.data[i])):
                        weight_element_sum += self.weights[i][j] * self.data[i][v]
                    weight_sum += self.weights[i][j]
                self.clusters = (weight_element_sum / weight_sum)


        def get_most_fit(self): # Want to minimize fitness
            fitness = [] # tuple: (fitness, index)
            for a in range(len(self.agents)):
                fitness.append(self.get_fitness(self.agents[a]))
            fitness.sort(key=lambda x: x[0])
            return fitness[0]

        def get_fitness(self, agent):
            for 
