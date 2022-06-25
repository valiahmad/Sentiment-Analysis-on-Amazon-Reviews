import re
import string
import nltk
import spacy
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from mysetting import mysetting
from const import review_score, review_text


              

def preprocessText(dataListed):

    nlp = spacy.load("en_core_web_sm")
    S = mysetting()                       #reading setting from file
    dataListPreprocessed = list()
    
    print('\n\nPreprocessing...')
    for i in range(0,len(dataListed)):
        txt = dataListed[i][review_text]#putting review text in txt

        txt = txt.lower()              #converting to lowercase
        txt = re.sub(r'\d+','',txt)    #deleting numbers
        txt = txt.translate(str.maketrans(\
            '','',string.punctuation)) #deleting punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        txt = txt.strip()



        #Tokenizing
        txtListTkn = list()
        if S['Tokenization'] == 'nltk':
            txtListTkn = word_tokenize(txt)
        

        elif S['Tokenization'] == 'spacy':
            txtDoc = nlp(txt)
            for word in txtDoc:
                if word.text != ' ':
                    txtListTkn.append(word.text)



        #deleting stopwords
        txtListStw = list()
        if S['StopWords'] == 'nltk':
            stopWords = set(stopwords.words('english'))
            txtListStw = [j for j in txtListTkn if not j in stopWords]
        

        elif S['StopWords'] == 'spacy':
            for word in txtDoc:
                if word.text != ' ' and word.is_stop == False:
                    txtListStw.append(word.text)



        #findind root
        txtListStemmed = list()
        if S['findingRoot'] == 'stemming' or S['findingRoot'] == 'both':
            stemmer = PorterStemmer()
            for word in txtListStw:
                txtListStemmed.append(stemmer.stem(word))
            
        else:
            txtListStemmed = txtListStw

        txtListLemmatized = list()
        if S['findingRoot'] == 'lemmatization' or S['findingRoot'] == 'both':
            lemmatizer = WordNetLemmatizer()
            for word in txtListStemmed:
                txtListLemmatized.append(lemmatizer.lemmatize(word))
            
        else:
             txtListLemmatized = txtListStemmed



        #POS Tagging
        txtTag = list()
        finalTxt = list()
        if S['POS Tagging'] == 'nltk':
            txtTagged = nltk.pos_tag(txtListLemmatized)
            for word in txtTagged:
                if word[1] == 'JJ':
                    txtTag.append(word[0])
            finalTxt = txtTag
        else:
            finalTxt = txtListLemmatized

    

        dataListPreprocessed.append([finalTxt, dataListed[i][review_score]])
        

        print('\r[%-20s] %d%% ' % ('#'*((i+1)//(len(dataListed)//20)),
        ((i+1)//(len(dataListed)//20))*5),end = '')
        


    return dataListPreprocessed