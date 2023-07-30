import math

from Consumer import Consumer
from Partition import Partition

from leastloaded2 import scaledLeastLoaded


import matplotlib.pyplot as plt




time = []
point = []
lamdasla = 85
replicas = []

wrkld = []


replicas = []
replicasscaled = []
partitions = []
wrkld = []
replicasbin = []
latencies = []

p0 = Partition("p0", 0, 0.0)
p1 = Partition("p1", 0, 0.0)
p2 = Partition("p2", 0, 0.0)
p3 = Partition("p3", 0, 0.0)
p4 = Partition("p4", 0, 0.0)




partitions = [p0, p1, p2, p3, p4]

currentBins = Consumer("0", partitions, 85.0 )





font = {'family': 'normal',
        'weight': 'bold',
        'size': 8}
def readWorkload():
    font = {'family': 'normal',
            'weight': 'bold',
            'size': 8}
    plt.rc('font', **font)
    with open('defaultArrivalRatesm.csv', 'r') as f:
        lines = f.readlines()

    for line in lines:
        sample = line.split(',')[1][0:-1]
        wrkld.append(math.ceil(float(sample)))
    return  wrkld


def plotWorkload():
    for i in range(len(wrkld)):
        time.append((i+1))
        point.append(wrkld[i])
    plt.plot(time, wrkld)
    plt.xlabel("Time (sec)", **font)
    plt.ylabel("Events/sec",**font)
    plt.show()


def computeReplicasLinearBinPackFraction():
    #600

    currentBins = [Consumer("0", partitions, 85.0)]
    for t in range(600):
        for p in range(5):
            partitions[p].lamda = point[t]/5.0

        # items = []
        # for i in range(5):
        #     items.append(part)
        #bins = LeastLoaded(items)

        ###########################################

        bins = scaledLeastLoaded(partitions, 1)

        replicasbin.append(len(bins))

        # elif len(bins) < len(currentBins):
        #     bins = scaledLeastLoaded(partitions, 1)
        #     if len(bins) < len(currentBins):
        #       replicasbin.append(len(bins))
        #       currentBins = bins
        #     else:
        #         replicasbin.append(len(currentBins))
        # else:
        #     replicasbin.append(len(currentBins))

        ##########################################
        #bins = scaledLeastLoaded(items, 1.0)
        #computeLatencies(point[t], bins)
        #replicasbin.append(bins)

    # print scaling actions:
    scalingActions = 0
    for t in range(599):
        if replicasbin[t] != replicasbin[t+1]:
            scalingActions += 1
    print("Scaling Actions is: " + str(scalingActions))


def plotWorkloadWithReplicasBinPack():
    replicasscaled = []
    for r in range(len(replicasbin)):
        replicasscaled.append(replicasbin[r]*85)

    plt.plot(time, wrkld)
    plt.plot(time, replicasscaled)
    plt.show()



if __name__ == '__main__':
    # testPartition()
    # testConsumer()
    readWorkload()
    plotWorkload()
    computeReplicasLinearBinPackFraction()
    plotWorkloadWithReplicasBinPack()



    #testLeastLoaded()