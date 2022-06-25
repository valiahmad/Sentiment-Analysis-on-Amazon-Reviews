from nltk.corpus import sentiwordnet as swn
from mysetting import mysetting

review_score = 1
review_txt_preprocessed = 0
##########################
oneStar = 1
twoStars = 2
threeStars = 3
fourStars = 4
fiveStars = 5
####################################


def calculate(dataSet):

    S = mysetting()
    

    numofStars = [0, 0, 0, 0, 0]
    listWordsofOneStar = [[],[]]
    listWordsofTwoStars = [[],[]]
    listWordsofThreeStars = [[],[]]
    listWordsofFourStars = [[],[]]
    listWordsofFiveStars = [[],[]]

    print('\n\nCounting Each Class...')
    for i in range(0,len(dataSet)):

        rtp = dataSet[i][review_txt_preprocessed]
        if S['method'] == 'binary':
            rtp = list(set(rtp))
        

        #one star
        if dataSet[i][review_score] == '1.0':
            numofStars[oneStar-1] += 1
            for word in rtp:
                if word in listWordsofOneStar[0]:#words in first row and repeattion of words in second row
                    listWordsofOneStar[1][listWordsofOneStar[0].index(word)] += 1
                else:
                    listWordsofOneStar[0].append(word)
                    listWordsofOneStar[1].append(1)
            


        #two stars
        elif dataSet[i][review_score] == '2.0':
            numofStars[twoStars-1] += 1
            for word in rtp:
                if word in listWordsofTwoStars[0]:#words in first row and repeattion of words in second row
                    listWordsofTwoStars[1][listWordsofTwoStars[0].index(word)] += 1
                else:
                    listWordsofTwoStars[0].append(word)
                    listWordsofTwoStars[1].append(1)


        #three stars
        elif dataSet[i][review_score] == '3.0':
            numofStars[threeStars-1] += 1
            for word in rtp:
                if word in listWordsofThreeStars[0]:#words in first row and repeattion of words in second row
                    listWordsofThreeStars[1][listWordsofThreeStars[0].index(word)] += 1
                else:
                    listWordsofThreeStars[0].append(word)
                    listWordsofThreeStars[1].append(1)


        #four stars
        elif dataSet[i][review_score] == '4.0':
            numofStars[fourStars-1] += 1
            for word in rtp:
                if word in listWordsofFourStars[0]:#words in first row and repeattion of words in second row
                    listWordsofFourStars[1][listWordsofFourStars[0].index(word)] += 1
                else:
                    listWordsofFourStars[0].append(word)
                    listWordsofFourStars[1].append(1)


        #five stars
        elif dataSet[i][review_score] == '5.0':
            numofStars[fiveStars-1] += 1
            for word in rtp:
                if word in listWordsofFiveStars[0]:#words in first row and repeattion of words in second row
                    listWordsofFiveStars[1][listWordsofFiveStars[0].index(word)] += 1
                else:
                    listWordsofFiveStars[0].append(word)
                    listWordsofFiveStars[1].append(1)
            
        

        print('\r[%-20s] %d%% ' % ('#'*((i+1)//(len(dataSet)//20)),
        ((i+1)//(len(dataSet)//20))*5),end = '')
    

    #all in one
    allListWords = listWordsofOneStar[0] + listWordsofTwoStars[0] +\
        listWordsofThreeStars[0] + listWordsofFourStars[0] +\
        listWordsofFiveStars[0]

    #unique words
    uniqueList = list(set(allListWords))

    #number of each class words
    sumofWordsOneStar = sum(listWordsofOneStar[1])
    sumofWordsTowStars = sum(listWordsofTwoStars[1])
    sumofWordsThreeStars = sum(listWordsofThreeStars[1])
    sumofWordsFourStars = sum(listWordsofFourStars[1])
    sumofWordsFiveStars = sum(listWordsofFiveStars[1])
    #number of all classes words
    allWords = sumofWordsOneStar + sumofWordsTowStars +\
        sumofWordsThreeStars + sumofWordsFourStars +\
        sumofWordsFiveStars

    
    #reporting
    if S['report'] == 'show':
        print('\n\nAll Words In All Classes : %d' % (allWords))
        print('Number of Unique Words : %d'% (len(uniqueList)))
        print('Number of Words of One Star : %d ' % (sumofWordsOneStar))
        print('Number of Words of Two Stars : %d ' % (sumofWordsTowStars))
        print('Number of Words of Three Stars : %d ' % (sumofWordsThreeStars))
        print('Number of Words of Four Stars : %d ' % (sumofWordsFourStars))
        print('Number of Words of Five Stars : %d ' % (sumofWordsFiveStars))
        print('Number of One Star Class : %d ' % (numofStars[0]))
        print('Number of Two Stars Class : %d ' % (numofStars[1]))
        print('Number of Three Stars Class : %d ' % (numofStars[2]))
        print('Number of Four Stars Class : %d ' % (numofStars[3]))
        print('Number of Five Stars Class : %d ' % (numofStars[4]))
        
        
    


    result = [len(uniqueList), numofStars,\
        [sumofWordsOneStar,\
        sumofWordsTowStars,\
        sumofWordsThreeStars,\
        sumofWordsFourStars,\
        sumofWordsFiveStars],\
        [listWordsofOneStar,\
        listWordsofTwoStars,\
        listWordsofThreeStars,\
        listWordsofFourStars,\
        listWordsofFiveStars],\
        allListWords]
    return result               
    """
    result[0]: number of unique words in dataset
    result[1]: included five elements that each of them shows number of that class in dataset
    result[2]: included five elements that each of them show number of words in that class
    result[3]: included five lists that each of them has a word and number repeated of that word
    
    """

###############################

def claProbability(dataSet):

    calculated = calculate(dataSet)
    #
    #
    numofUniqWords = calculated[0]
    #
    numofOneStarClassWords = calculated[2][0]
    numofTwoStarsClassWords = calculated[2][1]
    numofThreeStarsClassWords = calculated[2][2]
    numofFourStarsClassWords = calculated[2][3]
    numofFiveStarsClassWords = calculated[2][4]
    #
    wordsOneStar = calculated[3][0]
    wordsTwoStars = calculated[3][1]
    wordsThreeStars = calculated[3][2]
    wordsFourStars = calculated[3][3]
    wordsFiveStars = calculated[3][4]
    #
    #
    calProbOne = [[],[]]
    print('\nCalculating Probability of One Star...')
    for i in range(0,len(wordsOneStar[0])):
        calProbOne[0].append(wordsOneStar[0][i])
        calProbOne[1].append(\
            (wordsOneStar[1][i] + 1) / (numofOneStarClassWords + numofUniqWords))
        print('\r[%-20s] %d%% ' % ('#'*((i+1)//(len(wordsOneStar[0])//20)),
        ((i+1)//(len(wordsOneStar[0])//20))*5),end = '')
    
    
    calProbTwo = [[],[]]
    print('\nCalculating Probability of Two Stars...')
    for i in range(0,len(wordsTwoStars[0])):
        calProbTwo[0].append(wordsTwoStars[0][i])
        calProbTwo[1].append(\
            (wordsTwoStars[1][i] + 1) / (numofTwoStarsClassWords + numofUniqWords))
        print('\r[%-20s] %d%% ' % ('#'*((i+1)//(len(wordsTwoStars[0])//20)),
        ((i+1)//(len(wordsTwoStars[0])//20))*5),end = '')
    

    calProbThree = [[],[]]
    print('\nCalculating Probability of Three Stars...')
    for i in range(0,len(wordsThreeStars[0])):
        calProbThree[0].append(wordsThreeStars[0][i])
        calProbThree[1].append(\
            (wordsThreeStars[1][i] + 1) / (numofThreeStarsClassWords + numofUniqWords))
        print('\r[%-20s] %d%% ' % ('#'*((i+1)//(len(wordsThreeStars[0])//20)),
        ((i+1)//(len(wordsThreeStars[0])//20))*5),end = '')
    

    calProbFour = [[],[]]
    print('\nCalculating Probability of Four Stars...')
    for i in range(0,len(wordsFourStars[0])):
        calProbFour[0].append(wordsFourStars[0][i])
        calProbFour[1].append(\
            (wordsFourStars[1][i] + 1) / (numofFourStarsClassWords + numofUniqWords))
        print('\r[%-20s] %d%% ' % ('#'*((i+1)//(len(wordsFourStars[0])//20)),
        ((i+1)//(len(wordsFourStars[0])//20))*5),end = '')
    

    calProbFive = [[],[]]
    print('\nCalculating Probability of Five Stars...')
    for i in range(0,len(wordsFiveStars[0])):
        calProbFive[0].append(wordsFiveStars[0][i])
        calProbFive[1].append(\
            (wordsFiveStars[1][i] + 1) / (numofFiveStarsClassWords + numofUniqWords))
        print('\r[%-20s] %d%% ' % ('#'*((i+1)//(len(wordsFiveStars[0])//20)),
        ((i+1)//(len(wordsFiveStars[0])//20))*5),end = '')
    
    
    #
    calProbAll = [calProbOne, calProbTwo, calProbThree, calProbFour, calProbFive,
        calculated[1], calculated[0],calculated[4]]

    return calProbAll





def limClass(txt):

    pos = 0
    neg = 1
    rate = .013
    count = 0
    sentiList = [0,0]
    
    
    for word in txt:
        sentiSet = list(swn.senti_synsets(word))
        if len(sentiSet) == 0:
            continue
        else:
            count += 1
            sentiSet0 = sentiSet[0]
            sentiList[pos] += sentiSet0.pos_score()
            sentiList[neg] += sentiSet0.neg_score()
    
    
    if count:
        distance = abs((sentiList[pos]/count) - (sentiList[neg]/count))
    else:
        distance = 0
    
    result = sentiList.index(max(sentiList))
    
    if distance < rate:
        return [0,1,1,1,0]
    elif result == pos:
        return [0,0,1,1,1]
    elif result == neg:
        return [1,1,1,0,0]