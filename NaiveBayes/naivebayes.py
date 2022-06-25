import matplotlib.pyplot as plt
from NaiveBayes.calculating import claProbability
from NaiveBayes.calculating import limClass
from mysetting import mysetting
review_txt_preprocessed = 0
##########################
oneStar = 0
twoStars = 1
threeStars = 2
fourStars = 3
fiveStars = 4
####################################
#a LIST -> first index = TEXT and second index = LABEL
def naiveBayes(trainingData, testData):

    S = mysetting()
    
    calculatedData = claProbability(trainingData)
    #
    #
    calProbOne = calculatedData[0]
    calProbTwo = calculatedData[1]
    calProbThree = calculatedData[2]
    calProbFour = calculatedData[3]
    calProbFive = calculatedData[4]
    
    #
    numofOneStarClass = calculatedData[5][0]
    numofTwoStarsClass = calculatedData[5][1]
    numofThreeStarsClass = calculatedData[5][2]
    numofFourStarsClass = calculatedData[5][3]
    numofFiveStarsClass = calculatedData[5][4]
    #
    numofAllCalsses = sum(calculatedData[5])
    #
    numofUniqWords = calculatedData[6]
    #
    report = calculatedData[7]
    #
    POne = numofOneStarClass / numofAllCalsses
    PTwo = numofTwoStarsClass / numofAllCalsses
    PThree = numofThreeStarsClass / numofAllCalsses
    PFour = numofFourStarsClass / numofAllCalsses
    PFive = numofFiveStarsClass / numofAllCalsses
    #
    #
    participationOfClasses = [0,0,0,0,0]


    print('\n\nClassifying, Using %s...' % (S['method']))
    for i in range(0,len(testData)):

        txt = testData[i][review_txt_preprocessed]
        temp = [[],[]]
        scores = []
        

        if S['method'] == 'binary':
            txt = list(set(txt))
            participation = [1,1,1,1,1]
        elif S['method'] == 'binary&posneg':
            txt = list(set(txt))
            participation = limClass(txt)
        else:
            participation = [1,1,1,1,1]



        for word in txt:
            if word in temp[0]:
                temp[1][temp[0].index(word)] += 1
            else:
                temp[0].append(word)
                temp[1].append(1)
        
        
        #calculating for one star
        if participation[oneStar]:
            tempOne = 1
            participationOfClasses[oneStar] += 1 
            for word in temp[0]:
                if word in calProbOne[0]:
                    p = calProbOne[1][calProbOne[0].index(word)]
                    cofp = temp[1][temp[0].index(word)]
                    tempOne = cofp * p * tempOne
                else:
                    tempOne = 1 / (numofOneStarClass + numofUniqWords) * tempOne
            scores.append(tempOne * POne)
        else:
            scores.append(0)


        #calculating for two stars
        if participation[twoStars]:
            tempTwo = 1
            participationOfClasses[twoStars] += 1
            for word in temp[0]:
                if word in calProbTwo[0]:
                    p = calProbTwo[1][calProbTwo[0].index(word)]
                    cofp = temp[1][temp[0].index(word)]
                    tempTwo = cofp * p * tempTwo
                else:
                    tempTwo = 1 / (numofTwoStarsClass + numofUniqWords) * tempTwo
            scores.append(tempTwo * PTwo)
        else:
            scores.append(0)


        #calculating for three stars
        if participation[threeStars]:
            tempThree = 1
            participationOfClasses[threeStars] += 1
            for word in temp[0]:
                if word in calProbThree[0]:
                    p = calProbThree[1][calProbThree[0].index(word)]
                    cofp = temp[1][temp[0].index(word)]
                    tempThree = cofp * p * tempThree
                else:
                    tempThree = 1 / (numofThreeStarsClass + numofUniqWords) * tempThree
            scores.append(tempThree * PThree)
        else:
            scores.append(0)


        #calculating for four stars
        if participation[fourStars]:
            tempFour = 1
            participationOfClasses[fourStars] += 1
            for word in temp[0]:
                if word in calProbFour[0]:
                    p = calProbFour[1][calProbFour[0].index(word)]
                    cofp = temp[1][temp[0].index(word)]
                    tempFour = cofp * p * tempFour
                else:
                    tempFour = 1 / (numofFourStarsClass + numofUniqWords) * tempFour
            scores.append(tempFour * PFour)
        else:
            scores.append(0)


        #calculating for five stars
        if participation[fiveStars]:
            tempFive = 1
            participationOfClasses[fiveStars] += 1
            for word in temp[0]:
                if word in calProbFive[0]:
                    p = calProbFive[1][calProbFive[0].index(word)]
                    cofp = temp[1][temp[0].index(word)]
                    tempFive = cofp * p * tempFive
                else:
                    tempFive = 1 / (numofFiveStarsClass + numofUniqWords) * tempFive
            scores.append(tempFive * PFive)
        else:
            scores.append(0)

        
        
        result = scores.index(max(scores)) + 1
        testData[i].append(result)


        print('\r[%-20s] %d%% ' % ('#'*((i+1)//(len(testData)//20)),
        ((i+1)//(len(testData)//20))*5),end = '')


    
    report = [report,participationOfClasses]
        
    return testData,report