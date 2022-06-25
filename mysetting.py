import json

def mysetting(setting = None):
    
    if setting:
        f = open('setting.ssm', 'w')
        json.dump(setting,f)
        f.close()
        
        
    elif not setting:
        f = open('setting.ssm')
        setting = json.load(f)
        f.close()
        

    return setting


listofSet = [['\nChoose One For Tokenization : #1 NLTK   #2 SPACY : ',\
'Tokenization','nltk','spacy'],\
    ['\nChoose One For Deleting StopWords : #1 NLTK   #2 SPACY : ',\
    'StopWords','nltk','spacy'],\
    ['\nChoose One For Finding Root of Words : #1 Stemming   #2 Lemmatization   #3 Both #4 None : ',\
    'findingRoot','stemming','lemmatization', 'both', 'none'],\
    ['\nChoose One For POS Tagging : #1 NLTK   #2 None : ',\
    'POS Tagging','nltk','None'],\
    ['\nDo You Want To Show A Report Of Words : #1 Yes   #2 No : ',\
    'report','show','no'],\
    ['\nWhich Method Do You Want To Use : \n#1 Naive Bayes \n#2 Naive Bayes Binary \n#3 Binary & PosNeg \n',\
    'method','naivebayes', 'binary', 'binary&posneg']\
    ]

def setprog():
    i = 0
    S = dict()
    while True:
        option = input(listofSet[i][0])
        if option == '1':
            S[listofSet[i][1]] = listofSet[i][2]
            i += 1
        elif option == '2':
            S[listofSet[i][1]] = listofSet[i][3]
            i += 1
        elif option == '3':
            S[listofSet[i][1]] = listofSet[i][4]
            i += 1
        elif option == '4':
            S[listofSet[i][1]] = listofSet[i][5]
            i += 1
        else:
            print('\nPlease Try Againg!!! ')
        if i == len(listofSet):
            break
    return mysetting(S)