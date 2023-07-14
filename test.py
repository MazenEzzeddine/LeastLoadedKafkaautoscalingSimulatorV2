from Consumer import Consumer
from Partition import Partition

from leastloaded import scaledLeastLoaded


def testPartition():
    p0 = Partition("p0", 50.0, 0.0)
    p1 = Partition("p1", 25.0, 0.0)
    p2 = Partition("p2", 150.0, 0.0)
    p3 = Partition("p3", 75.0, 0.0)
    p4 = Partition("p4", 100.0, 0.0)
    print(p0>p1)
    print(p0 >= p1)
    print(p2)
    print(p3>p4)
    print (p4)








# Press the green button in the gutter to run the script.
def testConsumer():
    p0 = Partition("p0", 50.0, 0.0)
    p1 = Partition("p1", 25.0, 0.0)
    p2 = Partition("p2", 150.0, 0.0)
    p3 = Partition("p3", 75.0, 0.0)
    p4 = Partition("p4", 100.0, 0.0)

    c0 = Consumer("c0", [p0,p1],175)
    c1 = Consumer("c1", [p2,p3],175)

    c2 = Consumer("c2", [p4],100.0)

    print(c0)
    print(c1>c2)








def testLeastLoaded():
    bins = scaledLeastLoaded([85, 20, 30, 5, 80], 1)
    print(bins)





if __name__ == '__main__':
    testPartition()
    testConsumer()
    testLeastLoaded()