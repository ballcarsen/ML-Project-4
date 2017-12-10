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
        return self.globalBest.getClusters()

    def train(self, maxIterations):
        self.initParticles()
        self.optimizeSwarm(maxIterations)
        # return best fitness achieved
        return self.globalBest.getFitness()

    def initParticles(self):
        print("pop size", self.popSize)
        for index in range(self.popSize):
            #print("particle created: ")
            self.particles.append(Particle(self.data,self.k))
            self.particles[index].initialize()
        # set arbitrary global best to begin with
        self.globalBest = self.particles[0]

    def optimizeSwarm(self, maxIterations):
        iteration = 0
        while (iteration < maxIterations):
            self.findBest()
            print("iteration ", iteration)
            iteration += 1
            for indiv in self.particles:
                indiv.setGlobalBest(self.globalBest.getClusters())
                indiv.updateParticle()
        self.findBest()

    def findBest(self):
        for indiv in self.particles:
            print("global best fitness: ", self.globalBest.getFitness())
            if (indiv.getFitness() < self.globalBest.getFitness()):
                print("new best fitness: ", indiv.getFitness())
                self.globalBest = indiv



