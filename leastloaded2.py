from Consumer import Consumer
from Partition import Partition


def scaledLeastLoaded(partitions: list[Partition], f:float):
    partitions.sort(reverse=True)

    for partition in range(len(partitions)):
        print(partitions[partition])
    consCount = 1
    while True:
        consumers : list[Consumer] = []
        for i in range(consCount):
            consumer = Consumer(str(i), [],  85.0)
            consumers.append(consumer)

        for j in range(len(partitions)):
            consumers.sort(reverse=True)
            for id in range(consCount):
                if partitions[j].lamda < consumers[id].mu - consumers[id].getLamda():
                    consumers[id].partitions.append(partitions[j])
                    break
            else:
                consCount += 1
                break
        else:
            break
    return consumers

if __name__=='__main__':
    p0 = Partition("p0", 50.0, 0.0)
    p1 = Partition("p1", 25.0, 0.0)
    p2 = Partition("p2", 80.0, 0.0)
    p3 = Partition("p3", 75.0, 0.0)
    p4 = Partition("p4", 80.0, 0.0)
    partitions : list[Partition] = [p0,p1,p2,p3,p4]

    #print(partitions)

    for part in partitions:
        print(part)
        print("==============")
    scaledLeastLoaded(partitions, 1.0)