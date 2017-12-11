import math
from PSO.Particle import Particle
import calculations

# algorithm for clustering using PSO
class PSOClusterAlg:
    # initialize algorithm by setting parameters
    def __init__(self, data , k, popSize, c1, c2):
        self.c1 = c1
        self.c2 = c2
        self.data = data
        self.k = k # number of clusters
        self.popSize = popSize # number of particles
        self.particles = []

    # get best set of clusters generated
    def getBestClusters(self):
        return self.globalBest.getClusters()

    # our main method for pso, runs every stage of the algorithm
    def train(self, maxIterations):
        self.initParticles()
        self.optimizeSwarm(maxIterations)
        # return best fitness achieved
        return self.globalBest.getSilhouetteFitness()


    # initializes particles using kmeans to get initial clusters
    def initParticles(self):
        print("pop size", self.popSize)
        for index in range(self.popSize):
            self.particles.append(Particle(self.data,self.k,self.c1,self.c2 ))
            self.particles[index].initialize()
        # set arbitrary global best to begin with
        self.globalBest = self.particles[0]

    # after swarm is initialized, this method moves the particles towards optima
    def optimizeSwarm(self, maxIterations):
        iteration = 0
        while (iteration < maxIterations):
            self.findBest()
            print("iteration ", iteration)
            iteration += 1
            for indiv in self.particles:
                # make sure each particle has a reference to the current global best particle
                indiv.setGlobalBest(self.globalBest.getClusters())
                # move particles
                indiv.updateParticle()
        self.findBest()

    # method for finding the best particle in the swarm at the beginning of each iteration
    def findBest(self):
        currentGlobalBestFitness = self.globalBest.getSilhouetteFitness()
        print("global best fitness: ", currentGlobalBestFitness)
        for indiv in self.particles:
            indivFitness = indiv.getSilhouetteFitness()
            print("individual fitness ", indivFitness)
            if (indivFitness > currentGlobalBestFitness):
                print("new best fitness: ", indivFitness)
                self.globalBest = indiv
                currentGlobalBestFitness = self.globalBest.getSilhouetteFitness()



