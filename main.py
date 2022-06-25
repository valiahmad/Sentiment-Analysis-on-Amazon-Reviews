from Preprocessing.datasetToListStructure import dictToList
from Preprocessing.preprocessing import preprocessText
from sklearn import metrics
from calprecision import labeledDataToList, sortPrecisionList, precisionAve
from mysetting import setprog, mysetting
from indexing import makeIndex
from NaiveBayes.naivebayes import naiveBayes
import matplotlib.pyplot as plt
import wordcloud
import numpy as np
from myplot import plot_confusion_matrix
import time
import datetime


#setting of program
S = setprog()
# S = mysetting()

path = 'Software.txt.gz'
path2 = 'Gourmet_Foods.txt.gz'

if S['method'] == 'binary' or S['method'] == 'binary&posneg' or S['method'] == 'naivebayes':
    #create a list from dataset
    dataListed = dictToList(path)
    ###
    ##
    #
    #choosing how much for train and test
    dataListLength = len(dataListed)
    trainingDataLength = (90 * dataListLength) // 100
    testDataLength = (10 * dataListLength) // 100



    #preprocssing the text review
    txtPreprocessed = preprocessText(dataListed)


    k = dataListLength // testDataLength
    totalResult = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[]]
    myreport = [[],[0,0,0,0,0]]
    myarr = np.zeros((5,5), int)


    #cross validation
    for i in range(0,k):

        #partition rows for corss validation
        ind = makeIndex(i,dataListLength,trainingDataLength,testDataLength)
        trainingData = txtPreprocessed[ind[0]:ind[1]] + txtPreprocessed[ind[2]:ind[3]]
        testData = txtPreprocessed[ind[4]:ind[5]]


        #processing the text review
        #Naive Bayes
        startTime = time.process_time()
        dataLabeled, report = naiveBayes(trainingData, testData)
        endTime = time.process_time()
        takeTime = str(datetime.timedelta(seconds=endTime-startTime))
        print('\n\nNaive Bayes Has Done Successfuly in %s .' % (takeTime))
        myreport[0].extend(report[0])
        myreport[1][0] += report[1][0]
        myreport[1][1] += report[1][1]
        myreport[1][2] += report[1][2]
        myreport[1][3] += report[1][3]
        myreport[1][4] += report[1][4]
        #myreport[0] -> words of document
        #myreport[1][0] -> number of one-star class ets.
        #dataLabeled[0] -> TEXT
        #dataLabeled[1] -> True Label
        #dataLabeled[2] -> Predicted Label
        #calculating Precision, Recall, Accuracy
        result = labeledDataToList(dataLabeled)
        #result[0] --> the true score
        #result[1] --> the predicted score
        info = metrics.classification_report(result[0], result[1],output_dict = True,zero_division=1)
        arr = metrics.confusion_matrix(result[0], result[1])
        print(metrics.classification_report(result[0], result[1],zero_division=1))
        sortPrecisionList(info,totalResult, arr, myarr)
        print('='*60)


#LSTM
if S['method'] == 'lstm':
    startTime = time.process_time()
    #myLSTM(path)
    endTime = time.process_time()
    takeTime = str(datetime.timedelta(seconds=endTime-startTime))
    print('\n\nLSTM Has Done Successfuly in %s .' % (takeTime))

else:
    precisionAve(totalResult)
    common_words = str()
    for tokens in myreport[0]:
        common_words += ''.join(tokens)+' '
    _wordcloud = wordcloud.WordCloud().generate(common_words)
    plt.imshow(_wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('C:\\Users\\Vali Ahmad\\Desktop\\software_013.png',dpi=1200,bbox_inches='tight')
    plt.savefig('C:\\Users\\Vali Ahmad\\Desktop\\software_013.pdf',dpi=1200,bbox_inches='tight')
    plt.figure()
    plot_confusion_matrix(myarr,[1,2,3,4,5],cmap=plt.cm.Blues)
    # plt.savefig('E:\\Article\\result_0001_mat.png')
    # plt.savefig('E:\\Article\\result_0001_mat.pdf')
    if S['method'] == 'binary&posneg':
        plt.figure()
        plt.pie(myreport[1],labels=['One-Star','Two-Stars','Three-Stars','Four-Stars','Five-Stars']
            ,explode=[.1,.1,.1,.1,.1],autopct='%d%%')
        plt.title('Participated Classes')
        # plt.savefig('E:\\Article\\result_0001_pie.png')
        # plt.savefig('E:\\Article\\result_0001_pie.pdf')
    plt.show()