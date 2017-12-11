#!/usr/bin/env python3

import random
import math
import numpy as np # only used for random choice given probability distribution

class ACC():
    
    def __init__(self, epochs, ant_count, k, data, rho):
        self.epochs = epochs
        self.k = k # Number of clusters
        self.clusters = [] # Need to initialize somewhere
        self.data = data # Keep reference to data matrix
        self.weights = []
        self.pheromones = [] # data point x cluster
        self.agents = [] # Array of solution strings
        self.rho = rho # Tunable parameter
        self.init_weights() 
        self.g_best_index = 0
        self.init_colony(ant_count)
        self.init_pheromones()

    def cluster(self):
        for e in range(self.epochs):
            print(e)
            self.calc_cluster_average()
            #print(self.clusters, "\n\n")
            print(self.pheromones, "\n")
            #print(self.agents, "\n")
            self.generate_solutions()
            self.update_pheromones()

    def init_weights(self): # Initialize all of the weights
        for n in range(len(self.data)):
            cluster_vector = [] 
            for k in range(self.k):
                cluster_vector.append(0) # weight vectors should be zeros and a single one
            index = random.randint(0, self.k - 1) # Randomly assign cluster at the beginning
            cluster_vector[index] = 1 # randomly assign cluster initially
            self.weights.append(cluster_vector)

    def init_pheromones(self): # initialize the pheromone matrix
        for i in range(len(self.data)):
            pharaoh = []
            for j in range(self.k):
                pharaoh.append(random.uniform(0.1, 10)) # Uniformly select some floating point value to be the initial pheromone level for some given point
            self.pheromones.append(pharaoh)

    def init_colony(self, ants): # initialize the agents
        for a in range(ants):
            solution_string = []
            for n in range(len(self.data)):
                solution_string.append(random.randint(0, self.k - 1)) # Randomly generate some solution string
            self.agents.append(solution_string)

    def distance(self, vec_1, vec_2): # Euclidean distance squared
        sigma = 0
        for i in range(len(vec_1)): # assuming equal length
            sigma += (float(vec_1[i]) - vec_2[i])**2 # calculate squared euclidean distance
        return sigma

    def update_weights(self, agent): # Update weights with respect to the fittest individual
        for n in range(len(self.data)):
            cluster_vector = []
            for k in range(self.k):
                cluster_vector.append(0)
            cluster_vector[agent[n]] = 1 # Set weights to 1 to assimilate to most fit individual
            self.weights[n] = cluster_vector

    def update_pheromones(self):
        fittest = self.get_most_fit() # Retrieve the most fit individual
        self.update_weights(self.agents[fittest[1]]) # Update the weights
        print("Most Fit: %s" % fittest[0]) 
        for i in range(len(self.data)): 
            for j in range(self.k):
                delta_tao = self.weights[i][j] * (1 / fittest[0]) # Compete the change in pheromone with respect to the fittest individual
                #print(delta_tao)
                self.pheromones[i][j] = (self.pheromones[i][j] * (1 - self.rho)) + (self.rho * delta_tao) # Pheromone update

    def generate_solutions(self):
        # Clear old solutions
        temp = self.agents[self.g_best_index] # Get the agent with the most fit solution string
        for a in range(len(self.agents) - 1):
            self.agents[a] = []
        self.agents.append(temp)
        for i in range(len(self.data)):
            sigma = 0
            distribution = []
            choices = []
            for j in range(self.k):
                sigma += self.pheromones[i][j] # Sum the pheromones
            for j in range(self.k):
                distribution.append(self.pheromones[i][j] / sigma) # compute probability distribution of each cluster option with respect to the pheromone levels
                choices.append(j) # generate choices (simple array of consecutive integers
            for a in self.agents:
                #print(distribution)
                a.append(np.random.choice(choices, None, p=distribution)) # Generate new solution strings for each agent

    def calc_cluster_average(self):
        # clear clusters
        self.clusters = []
        for j in range(self.k):
            mean = [] # i, v
            for v in range(len(self.data[0])):
                weight_sum = 0
                weight_element_sum = 0
                for i in range(len(self.data)):
                    weight_sum += self.weights[i][j] # calculate sum of weights in class j
                    weight_element_sum += self.weights[i][j] * float(self.data[i][v]) # calculate sum of products of weights in class j by the data point i,v
                if weight_sum == 0: # if no item in class j
                    mean.append(0) # zero mean
                else:
                    mean.append(weight_element_sum / weight_sum) # Compute mean
            self.clusters.append(mean)


    def get_most_fit(self): # Want to minimize fitness
        fitness = [] # tuple: (fitness, index)
        for a in range(len(self.agents)):
            fitness.append((self.get_fitness(self.agents[a]), a))
        fitness.sort(key=lambda x: x[0]) # get ascending order of fitness
        sigma = 0
        for f in fitness:
            sigma += f[0] # sum fitness results
        #print(fitness)
        fit = fitness[0][0] / sigma # normalize fitnesses
        self.g_best_index = fitness[0][1] # set global best agent (index of)
        return (fit, fitness[0][1]) # Return most fit

    def get_fitness(self, agent):
        sigma = 0
        for j in range(self.k):
            for i in range(len(self.data)):
                if agent[i] == self.weights[i][j]:
                    sigma += self.distance(self.data[i], self.clusters[j]) # Sum distances
        return sigma # Return the fitness of current agent
