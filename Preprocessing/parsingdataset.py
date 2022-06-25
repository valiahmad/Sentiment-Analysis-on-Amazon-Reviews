import gzip
import json
import simplejson

def parse(filename):
    f = gzip.open(filename, 'r')
    entry = {}
    for l in f:
        l = l.strip()
        colonPos = l.decode(encoding="utf_8").find(':')
        if colonPos == -1:
            yield entry
            entry = {}
            continue
        eName = l[:colonPos]
        rest = l[colonPos+2:]
        entry[eName] = rest
    yield entry
########################################################
def readFile(address):
    datasetDict = dict()
    count = 0
    end = 1000       #number of sample(s)
    print('\nReading From File...')
    for e in parse(address):
        datasetDict[str(count)] = json.loads(simplejson.dumps(e))
        count += 1
        print('\r[%-20s] %d%% ' % ('#' * (count//(end//20)), count//(end//20)*5), end = '')
        if count == end:
            break
    return datasetDict