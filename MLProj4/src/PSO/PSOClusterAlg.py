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

    def train(self, maxIterations):
        self.initParticles()
        self.optimizeSwarm(maxIterations)
        # return best fitness achieved
        self.findBest()
        return self.globalBest.getSilhouetteFitness()



    def initParticles(self):
        print("pop size", self.popSize)
        for index in range(self.popSize):
            #print("particle created: ")
            self.particles.append(Particle(self.data,self.k,self.c1,self.c2 ))
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
            print("global best fitness: ", self.globalBest.getSilhouetteFitness())
            if (indiv.getSilhouetteFitness() > self.globalBest.getSilhouetteFitness()):
                print("new best fitness: ", indiv.getSilhouetteFitness())
                self.globalBest = indiv



