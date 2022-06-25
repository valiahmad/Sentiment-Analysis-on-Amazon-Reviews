
def makeIndex(i, dataSetLength, amountofTrain, amountofTest):
    ind = []
    ex = 0
    ind.append(i * amountofTest)
    ind.append(ind[0] + amountofTrain)
    if ind[1] > dataSetLength:
        ex = ind[1] - dataSetLength
        ind[1] = dataSetLength
    ind.append(0)
    ind.append(ex)
    if i >= 1:
        ind.append(ind[3])
        ind.append(ind[3] + amountofTest)
    else:
        ind.append(ind[1])
        ind.append(ind[1] + amountofTest)
    return ind