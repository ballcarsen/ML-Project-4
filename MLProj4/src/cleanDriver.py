from Data import Data
import numpy.random as rand
from Competetive.network import Network
from KMeans.KMeans import KMeans
from PSO.PSOClusterAlg import  PSOClusterAlg
import calculations
from dbScan import dbScan
fileName = 'seeds'
d1 = Data(2)
d1.readData(fileName + '.txt')
d1.scale()
d1.getFolds()
data = d1.crossValidatedTrain[0]
for i in d1.crossValidatedTest[0]:
    data.append(i)
k = 20
learningRates = [.5, .05, .01, .005, .001]
kParams = [4, 8, 12, 16]
minPoints = [50, 30, 20, 15, 10, 5, 3]
epsilon = [.7, .5, .3, .2, .1, .09, .07, .04, .01, .008, .002]
#kParams = [k * len(data) for k in kParams]
#kParams = [round(k) for k in kParams]

def runK(data, k):
    k1 = KMeans(data, k)
    k1.cluster()
    k1.reCluster()
    return(k1.getFitness())
def multiRunK():
    kFits = []
    for i in range(len(kParams)):
        kFits.append([kParams[i]])
        for k in range(30):
            fitness = runK(data, kParams[i])
            kFits[i].append(fitness)
    with open('KMeans' + fileName + 'Out', 'w') as out:
        for i in kFits:
            out.write(str(i))
            out.write('\n')
def runNet(data, k, learningRate):
    N1 = Network(data, k, learningRate)
    N1.makeNet()
    N1.train()
    return(N1.getFitness())
def multiRunNet():
    netFits = []
    for i in range(len(kParams)):
        for k in range(len(learningRates)):
            netFits.append([kParams[i], learningRates[k]])
            for j in range(30):
                print(kParams[i], ' ',learningRates[k], ' iter ', j)
                fitness = runNet(data, kParams[i], learningRates[k])
                netFits[i].append(fitness)
    with open('CompNet' + fileName + 'Out', 'w') as out:
        for i in netFits:
            out.write(str(i))
            out.write('\n')
def runDB(data, minPoints, epsilon):
    d1 = dbScan(minPoints, epsilon, data)
    return(d1.run())
def multiRunDB():
    for i in range(len(minPoints)):
        for k in range(len(epsilon)):
            print(runDB(data, minPoints[i], epsilon[k]), ' ', minPoints[i], epsilon[k])
multiRunDB()
#multiRunK()
#multiRunNet()

def runPSO(data):
    pso = PSOClusterAlg(data, k, 50)
    avgFitness = pso.train(20)
    bestClusters = pso.getBestClusters()
    myData = []
    '''
    for c in bestClusters:
        myData.append(c.clusterPoints)
    calculations.graph(myData, k)
    '''
    print("PSO fitness: ", avgFitness)

#runPSO(data)
