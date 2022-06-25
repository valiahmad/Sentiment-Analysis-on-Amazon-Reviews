from statistics import mean
review_score = 1
review_labeled_score = 2


def labeledDataToList(dataLabeled):

    trueList = list()
    for i in range(0,len(dataLabeled)):
        if dataLabeled[i][review_score] == '1.0':
            trueList.append(1)

    
    for i in range(0,len(dataLabeled)):
        if dataLabeled[i][review_score] == '2.0':
            trueList.append(2)


    for i in range(0,len(dataLabeled)):
        if dataLabeled[i][review_score] == '3.0':
            trueList.append(3)


    for i in range(0,len(dataLabeled)):
        if dataLabeled[i][review_score] == '4.0':
            trueList.append(4)


    for i in range(0,len(dataLabeled)):
        if dataLabeled[i][review_score] == '5.0':
            trueList.append(5)



    predictedList = list()
    for i in range(0,len(dataLabeled)):
        if dataLabeled[i][review_labeled_score] == 1:
            predictedList.append(1)


    for i in range(0,len(dataLabeled)):
        if dataLabeled[i][review_labeled_score] == 2:
            predictedList.append(2)


    for i in range(0,len(dataLabeled)):
        if dataLabeled[i][review_labeled_score] == 3:
            predictedList.append(3)


    for i in range(0,len(dataLabeled)):
        if dataLabeled[i][review_labeled_score] == 4:
            predictedList.append(4)


    for i in range(0,len(dataLabeled)):
        if dataLabeled[i][review_labeled_score] == 5:
            predictedList.append(5)


    result = [trueList, predictedList]
    return result




def sortPrecisionList(info,totalResult, arr, myarr):

    totalResult[0][0].append(info['1']['precision'])
    totalResult[0][1].append(info['1']['recall'])
    totalResult[0][2].append(info['1']['f1-score'])

    totalResult[1][0].append(info['2']['precision'])
    totalResult[1][1].append(info['2']['recall'])
    totalResult[1][2].append(info['2']['f1-score'])

    totalResult[2][0].append(info['3']['precision'])
    totalResult[2][1].append(info['3']['recall'])
    totalResult[2][2].append(info['3']['f1-score'])

    totalResult[3][0].append(info['4']['precision'])
    totalResult[3][1].append(info['4']['recall'])
    totalResult[3][2].append(info['4']['f1-score'])

    totalResult[4][0].append(info['5']['precision'])
    totalResult[4][1].append(info['5']['recall'])
    totalResult[4][2].append(info['5']['f1-score'])

    totalResult[5].append(info['accuracy'])

    ########################################

    for i in range(0,5):
        for j in range(0,5):
            myarr[i][j] += arr[i][j]





def precisionAve(result):

    # print('Precison 1 : %f' % (sum(result[0][0]) / len(result[0][0])))
    # print('Recall 1 : %f' % (sum(result[0][1]) / len(result[0][1])))
    # print('F1-score 1 : %f' % (sum(result[0][2]) / len(result[0][2])))

    # print('Precison 2 : %f' % (sum(result[1][0]) / len(result[1][0])))
    # print('Recall 2 : %f' % (sum(result[1][1]) / len(result[1][1])))
    # print('F1-score 2 : %f' % (sum(result[1][2]) / len(result[1][2])))

    # print('Precison 3 : %f' % (sum(result[2][0]) / len(result[2][0])))
    # print('Recall 3 : %f' % (sum(result[2][1]) / len(result[2][1])))
    # print('F1-score 3 : %f' % (sum(result[2][2]) / len(result[2][2])))

    # print('Precison 4 : %f' % (sum(result[3][0]) / len(result[3][0])))
    # print('Recall 4 : %f' % (sum(result[3][1]) / len(result[3][1])))
    # print('F1-score 4 : %f' % (sum(result[3][2]) / len(result[3][2])))

    # print('Precison 5 : %f' % (sum(result[4][0]) / len(result[4][0])))
    # print('Recall 5 : %f' % (sum(result[4][1]) / len(result[4][1])))
    # print('F1-score 5 : %f' % (sum(result[4][2]) / len(result[4][2])))

    # print('Accuracy : %f' % (sum(result[5]) / len(result[5])))

    # print('\n\nPrecison : %f' % ((mean(result[0][0])+mean(result[1][0])+
    # mean(result[2][0])+mean(result[3][0])+mean(result[4][0])) / 5))
    # print('\nRecall : %f' % ((mean(result[0][1])+mean(result[1][1])+
    # mean(result[2][1])+mean(result[3][1])+mean(result[4][1])) / 5))
    # print('\nF1-score : %f' % ((mean(result[0][2])+mean(result[1][2])+
    # mean(result[2][2])+mean(result[3][2])+mean(result[4][2])) / 5))
    print((sum(result[0][0]) / len(result[0][0])))
    print((sum(result[0][1]) / len(result[0][1])))
    print((sum(result[0][2]) / len(result[0][2])))

    print((sum(result[1][0]) / len(result[1][0])))
    print((sum(result[1][1]) / len(result[1][1])))
    print((sum(result[1][2]) / len(result[1][2])))

    print((sum(result[2][0]) / len(result[2][0])))
    print((sum(result[2][1]) / len(result[2][1])))
    print((sum(result[2][2]) / len(result[2][2])))

    print((sum(result[3][0]) / len(result[3][0])))
    print((sum(result[3][1]) / len(result[3][1])))
    print((sum(result[3][2]) / len(result[3][2])))

    print((sum(result[4][0]) / len(result[4][0])))
    print((sum(result[4][1]) / len(result[4][1])))
    print((sum(result[4][2]) / len(result[4][2])))
    print('')
    print((sum(result[5]) / len(result[5])))
    print('')
    print(((mean(result[0][0])+mean(result[1][0])+
    mean(result[2][0])+mean(result[3][0])+mean(result[4][0])) / 5))
    print(((mean(result[0][1])+mean(result[1][1])+
    mean(result[2][1])+mean(result[3][1])+mean(result[4][1])) / 5))
    print(((mean(result[0][2])+mean(result[1][2])+
    mean(result[2][2])+mean(result[3][2])+mean(result[4][2])) / 5))