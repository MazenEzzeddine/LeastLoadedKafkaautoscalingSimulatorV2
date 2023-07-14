from Partition import Partition


class  Consumer(object):
    def __init__(self, id = "", partitions: list[Partition]= None, mu =0.0):
        if partitions is None:
            partitions = []
        self.partitions = partitions
        self.mu = mu
        self.id = id
    def __str__(self):
        str1 =   "consumer %s mu: %f lamda: %f  lag : %f"  % (self.id, self.mu, self.getLamda(),  self.getLag())
        str2 = ' '.join([' %s' % (self.partitions[n]) for n in range(len(self.partitions))])
        return str1 + " partitions " + str2

    def __eq__(self, other):
        return self.partitions == other.partitions and self.mu == other.mu
        # need to be redefined.

    def __lt__(self, other):
        return self.getLamda() < other.getLamda()

    def __gt__(self, other):
        return self.getLamda() > other.getLamda()

    def __le__(self, other):
        return self.getLamda() <= other.getLamda()

    def __ge__(self, other):
        return self.getLamda() >= other.getLamda()

    def getLag(self):
        lag = 0.0
        for p in self.partitions:
            lag += p.lag
        return lag


    def getLamda(self):
        lamda = 0.0
        for p in self.partitions:
            lamda += p.lamda
        return lamda




