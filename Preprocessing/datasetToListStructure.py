from Preprocessing.parsingdataset import readFile

def dictToList(address):

    sortedList = []
    unsortedList = readFile(address)
    
    print('\n\nConverting Dictionary To List...')
    for i in range(0,len(unsortedList)):
        sortedList.append([unsortedList[str(i)]['product/productId'],unsortedList[str(i)]['product/title'],
        unsortedList[str(i)]['product/price'],unsortedList[str(i)]['review/userId'],
        unsortedList[str(i)]['review/profileName'],unsortedList[str(i)]['review/helpfulness'],
        unsortedList[str(i)]['review/score'],unsortedList[str(i)]['review/time'],
        unsortedList[str(i)]['review/summary'],unsortedList[str(i)]['review/text']])
        print('\r[%-20s] %d%% ' % ('#'*((i+1)//(len(unsortedList)//20)),
        ((i+1)//(len(unsortedList)//20))*5),end = '')
    return sortedList