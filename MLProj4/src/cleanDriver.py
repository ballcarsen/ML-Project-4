#imports
from Data import Data
import numpy as np
import numpy.random as rand
from Competetive.network import Network
from KMeans.KMeans import KMeans
from PSO.PSOClusterAlg import  PSOClusterAlg
import calculations
from dbScan import dbScan

#A driver used to make multiple calls to different algorithms

fileName = 'shuttle.trim'
d1 = Data(2)
d1.readData(fileName + '.txt')
d1.scale()
d1.getFolds()
data = d1.crossValidatedTrain[0]
for i in d1.crossValidatedTest[0]:
    data.append(i)
learningRates = [.5, .05, .01, .005, .001]
kParams = [2,4,8, 16]
minPoints = [0.25, 0.15, 0.1, 0.07, 0.05, 0.03, 0.01]
minPoints = [point * len(data) for point in minPoints]
minPoints = [round(min) for min in minPoints]
epsilon = [.7, .5, .3, .2, .1, .05]
#kParams = [k * len(data) for k in kParams]
#kParams = [round(k) for k in kParams]

k = 5


def runK(data, k):
    k1 = KMeans(data, k)
    k1.cluster()
    k1.reCluster()
    return(k1.getFitness())

def multiRunK():
    kFits = []
    for i in range(len(kParams)):
        kFits.append([kParams[i]])
        for k in range(5):
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
    count = 0
    for i in range(len(kParams)):
        for k in range(len(learningRates)):
            netFits.append([kParams[i], learningRates[k]])
            for j in range(5):
                print(kParams[i], ' ',learningRates[k], ' iter ', j)
                fitness = runNet(data, kParams[i], learningRates[k])
                netFits[count].append(fitness)
            count += 1
    with open('CompNet' + fileName + 'Out', 'w') as out:
        for i in netFits:
            out.write(str(i))
            out.write('\n')
def runDB(data, minPoints, epsilon):
    d1 = dbScan(minPoints, epsilon, data)
    return(d1.run())
dbResults = []
dbResults.append([['Fit'], ['Sil'], ['numClusters'], ['Percent Noise'], ['Min Points'], ['Distance']])

def multiRunDB():

    for i in range(len(minPoints)):
        for k in range(len(epsilon)):
            print(runDB(data, minPoints[i], epsilon[k]), ' ', minPoints[i], epsilon[k])
            res = runDB(data, minPoints[i], epsilon[k])
            res.append([minPoints[i]])
            res.append(epsilon[k])
            dbResults.append(res)
#multiRunDB()
#for i in dbResults:
    #print(i)
#dbToSave = np.array(dbResults)
#np.savetxt('db' + fileName + 'out', dbToSave)
#multiRunNet()
#multiRunK()


def runPSO(data,k,pop,c1,c2):
    # parameters: dataset, k , population size, global effect scalar (c1), local effect scalar (c2)
    pso = PSOClusterAlg(data, k, pop,c1,c2)
    fitness = pso.train(3)
    return(fitness)
    '''
    bestClusters = pso.getBestClusters()
    myData = []
    for c in bestClusters:
        myData.append(c.clusterPoints)
    calculations.graph(myData, k)
    '''
out = []
out.append([6, 20, 4, 8])
for k in range(1):
    out.append(runPSO(data,6,20,4,8))
for i in out:
    print(i)

