

def scaledLeastLoaded(items, f):
    for i in range(len(items)):
        print(items[i])

    items.sort(reverse=True)
    bincount = 1

    while True:
        bins = []
        for i in range(bincount):
            bin = 87*f
            bins.append(bin)

        for j in range(len(items)):
            bins.sort(reverse=True)
            for id in range(bincount):
                if items[j] < bins[id]:
                    bins[id] = bins[id] - items[j]
                    break
            else:
                bincount += 1
                break
        else:
            break
    print(bincount)
    return bincount