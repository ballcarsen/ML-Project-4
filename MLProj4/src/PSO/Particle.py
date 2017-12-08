from KMeans.KMeans import KMeans
from KMeans.cluster import Cluster
import random

class Particle:

    def __init__(self, data , k ):
        self.data = data
        self.k = k
        self.personalBest = [[]]
        self.globalBest = [[]]
        self.kMeans = KMeans(self.data, self.k)
        self.fitness = 0
        self.velocity = []
        self.clusters = []

    def getClusters(self):
        return self.clusters

    # initialize initial centers using KMeans
    def initialize(self):
        # cluster and recluster using kMeans
        self.kMeans.cluster()
        self.kMeans.reCenter()
        # get clusters from kMeans
        self.clusters = self.kMeans.clusters
        # set initial fitness and current best fitness
        self.fitness = 0.0
        self.fitness = self.kMeans.getFitness()
        self.bestFitness = self.fitness
        # assign personal best to initial location
        self.personalBest = self.clusters
        # set initial velocity to zero
        for center in range(len(self.clusters)):
            self.velocity.append([])
            for attribute in range(len(self.clusters[0].mean)):
                self.velocity[center].append(0)
        print(self.velocity)


    def updateParticle(self):
        # update velocity
        self.updateVelocity()
        # move particle towards personal and global best
        self.move()
        # is this statement necessary?
        self.kMeans.setClusters(self.clusters)
        self.kMeans.cluster()
        self.kMeans.reCenter()
        self.fitness = self.kMeans.getFitness()
        #self.updatePersonalBest()

    # move particle towards personal and global best
    def move(self):
        # move particle based on new velocity
        for center in range(len(self.clusters)):
            for attribute in range(len(self.clusters[0].mean)):
                self.clusters[center].mean[attribute] = self.velocity[center][attribute] + self.clusters[center].mean[attribute]

    # update particle velocity
    def updateVelocity(self):
        #for every attribute of every center: set velocity
        for center in range(len(self.clusters)):
            for attribute in range(len(self.clusters[0].mean)):
                # generate random numbers for velocity update
                rand1 = random.uniform(0.0,1.0)
                rand2 = random.uniform(0.0,1.0)
                # set new velocity equals the old velocity plus terms with global and personal best
                '''
                print(len(self.globalBest[0].mean))
                print(len(self.clusters[0].mean))
                print(len(self.velocity[0]))

                print(len(self.globalBest))
                print(len(self.clusters))
                print(len(self.velocity))

                print(self.globalBest[center].mean[attribute])
                print(self.clusters[center].mean[attribute])
                
                print("velocity " , self.velocity[center][attribute])
                '''

                self.velocity[center][attribute] = self.velocity[center][attribute] + \
                                                   ((rand1 * (self.globalBest[center].mean[attribute] - self.clusters[center].mean[attribute]))) + \
                                                   ((rand2 * (self.personalBest[center].mean[attribute] - self.clusters[center].mean[attribute])))


    def updatePersonalBest(self):
        if(self.fitness > self.bestFitness):
            self.personalBest = self.clusters

    def setGlobalBest(self, best):
        self.globalBest = best

    def getFitness(self):
        return self.fitness