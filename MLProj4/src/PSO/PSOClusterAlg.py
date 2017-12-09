import math
from PSO.Particle import Particle

class PSOClusterAlg:

    def __init__(self, data , k, popSize ):
        self.data = data
        self.k = k # number of clusters
        self.popSize = popSize # number of particles
        self.particles = []

    # get best set of clusters generated
    def getBestClusters(self):
        return self.findBest().getClusters()

    def train(self, maxIterations):
        self.initParticles()
        self.optimizeSwarm(maxIterations)
        # return best fitness achieved
        return self.averageFitness()

    def averageFitness(self):
        sum = 0
        for cluster in self.findBest().getClusters():
            sum += cluster.calcFitness()
        return sum


    def initParticles(self):
        for index in range(self.popSize):
            self.particles.append(Particle(self.data,self.k))
            self.particles[index].initialize()

    def optimizeSwarm(self, maxIterations):
        iteration = 0
        bestIndiv = self.findBest()
        while (iteration < maxIterations):
            iteration += 1
            for indiv in self.particles:
                indiv.setGlobalBest(bestIndiv.getClusters())
                indiv.updateParticle()


    def findBest(self):
        fitness = math.inf
        bestIndiv = None
        for indiv in self.particles:
            if (indiv.getFitness() < fitness):
                fitness = indiv.getFitness()
                bestIndiv = indiv
        return bestIndiv



