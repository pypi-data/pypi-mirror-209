# Libraries

# Cloud libraries
import boto3
from botocore.exceptions import ClientError


import pandas as pd
import random
import re, nltk, spacy, gensim
from newspaper import Article
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import pathlib
import numpy as np
import warnings
from datetime import date, datetime, timedelta
from dateutil.parser import parse
import io
from simple_colors import *
import time
import sys
import itertools
import threading

# NLTK
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
stop_words=set(nltk.corpus.stopwords.words('english'))

# Sklearn
from sklearn.decomposition import LatentDirichletAllocation, TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from pprint import pprint

# Plotting tools
import pyLDAvis
import pyLDAvis.sklearn
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import warnings
warnings.filterwarnings("ignore")

# Main Files - Global Variables

sts_client = boto3.client('sts')
assumed_role_object=sts_client.assume_role(
    RoleArn="arn:aws:iam::278808910769:role/JupyterS3FullAccessRole",
    RoleSessionName="gdelt-session-1"
)

credentials=assumed_role_object['Credentials']

boto3_session = boto3.session.Session(
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'], 
    aws_session_token=credentials['SessionToken']
)

s3 = boto3.resource('s3')
bucket = s3.Bucket('gdelt-all')
s4=boto3_session.client('s3')

def remove_duplicates(l):
    return list(set(l))



# 2.2 Clean data for the LDA Analysis

def clean_text(headline):
    le=WordNetLemmatizer()
    word_tokens=word_tokenize(headline)
    tokens=[le.lemmatize(w) for w in word_tokens if w not in stop_words and len(w)>3]
    cleaned_text=" ".join(tokens)
    return cleaned_text

# 2.3 get v1-counts

# Common Functions

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rWorking on your request ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!')

def vwordc(data3):
    text = ''.join(data3)
    # max no. of characters allowed by python
    if len(text) > 1000000:
        text = text[:1000000]
    per = 0.05
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    summary1 = ' '.join([w for w in summary.split() if len(w)>3])
    wordcloud = WordCloud(width= 1000, height = 600, max_words=1000,
                          random_state=1, background_color='gray', colormap='viridis_r',
                          collocations=False, stopwords = STOPWORDS).generate(summary1)
    fig = plt.figure()
    plt.figure(figsize=(30, 20))
    plt.imshow(wordcloud) 
    plt.axis("off")
    plt.savefig('Events.png', dpi = 1000)
    plt.close(fig)    


        
    
def vlda(r2):
    data4 = pd.DataFrame(r2)
    data5=data4[0].apply(clean_text)
    vect =TfidfVectorizer(stop_words=stop_words,max_features=1000)
    vect_text=vect.fit_transform(data5)
    lda_model=LatentDirichletAllocation(n_components=20,
    learning_method='online',random_state=42,max_iter=1) 
    lda_top=lda_model.fit_transform(vect_text)
    vocab = vect.get_feature_names()
    with open("lda-analysis.txt", 'w') as myfile:
        for i, comp in enumerate(lda_model.components_):
            vocab_comp = zip(vocab, comp)
            sorted_words = sorted(vocab_comp, key= lambda x:x[1], reverse=True)[:20]
            var1 = "Topic "+str(i+1)+": "
            myfile.writelines(var1)
            myfile.write("\n")
            for t in sorted_words:
                var2 = t[0]
                myfile.writelines(var2)
                var3 = " "
                myfile.writelines(var3)
            var4 = "\n"
            myfile.writelines(var4)
    myfile.close()

    
 #print(t[0], end=" ")   

# V1COUNTS FAMILY ############################################################################

def vcounts1(x):
    # V1-Counts
    datew=x
    key = 'v1/dt=' + x + '/' + x + '-cameo-counts.parquet'
    try:

        obj = s4.get_object(Bucket='gdelt-all', Key=key)
        df1 = pd.read_parquet(io.BytesIO(obj['Body'].read()))
        return df1

    except ClientError as ex:
        if ex.response['Error']['Code'] == 'NoSuchKey':
            print("No info for the dates provided")
            return


def vcounts21(df1):
    
    # Injesting the pandas dataframe
    wsources = list(df1['SOURCEURLS'])
    # wsources = random.sample(wsources, int(len(wsources)*0.001))
    data = ''.join(wsources)
    data = data.split("htt")
        # Cleaning

    # Cleaning

    data2 = []

    for line in data:
        line2 = pathlib.PurePath(line).name
        if not re.match(r"^article", line2):
            if not re.match(r'^[0-9].*', line2):
                data2.append(line2)

    clean_txt = []
    for lines in data2:
        desc = lines.lower()

        #remove punctuation
        desc = re.sub('[^a-zA-Z]', ' ', desc)

        #remove tags
        desc=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",desc)

        #remove digits and special chars
        desc=re.sub("(\\d|\\W)+"," ",desc)

        desc=desc.replace("-", ' ')

        desc=desc.replace("html", '')
        desc=desc.replace("<UDIV>", '')
        desc=desc.replace("udiv", '')
        clean_txt.append(desc)    



    for i in clean_txt[:]:
        if len(i) <= 25:
            clean_txt.remove(i)

    data3=[]
    for i in clean_txt:
        data3.append(i.strip())


    # to remove duplicated
    # from list
    def remove_duplicates(l):
        return list(set(l))
    data3 = remove_duplicates(data3)    
    df3 = pd.DataFrame(data3)
    df3.to_csv(r'HeadnewsV1Counts.csv', index = None, header=True)
    return data3


        
#V1-GKG FAMILY##########################################################################

        
        
        
def vgkg1(x):
    # V1 - gkg
    key = 'v1/dt=' + x + '/' + x + '-cameo-gkg.parquet'
    try:
        obj = s4.get_object(Bucket='gdelt-all', Key=key)
        df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
        return df
                
    except ClientError as ex:
        if ex.response['Error']['Code'] == 'NoSuchKey':
            print("No info for the dates provided")
            return                

def vgkg21(df1):        
    wsources = list(df1['SOURCEURLS'])
    # wsources = random.sample(wsources, int(len(wsources)*0.001))
    data = ''.join(wsources)
    data = data.split("htt")
        # Cleaning

    # Cleaning

    data2 = []

    for line in data:
        line2 = pathlib.PurePath(line).name
        if not re.match(r"^article", line2):
            if not re.match(r'^[0-9].*', line2):
                data2.append(line2)

    clean_txt = []
    for lines in data2:
        desc = lines.lower()

        #remove punctuation
        desc = re.sub('[^a-zA-Z]', ' ', desc)

        #remove tags
        desc=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",desc)

        #remove digits and special chars
        desc=re.sub("(\\d|\\W)+"," ",desc)

        desc=desc.replace("-", ' ')

        desc=desc.replace("html", '')
        desc=desc.replace("<UDIV>", '')
        desc=desc.replace("udiv", '')
        clean_txt.append(desc)    



    for i in clean_txt[:]:
        if len(i) <= 25:
            clean_txt.remove(i)

    data3=[]
    for i in clean_txt:
        data3.append(i.strip())


    # to remove duplicated
    # from list
    def remove_duplicates(l):
        return list(set(l))
    data3 = remove_duplicates(data3)    
    df3 = pd.DataFrame(data3)
    df3.to_csv(r'HeadnewsV1GKG.csv', index = None, header=True)
    return data3
        
#V2-ENG-EXP FAMILY##########################################################################
        
def engexport1(x):
    # V2 English-Export
    prefix = 'v2/dt=' + x + '/'
    startsw = 'v2/dt=' + x + '/' + x + '-en-export'
    dfa = []
    for obj in bucket.objects.filter(Prefix=prefix):
        if obj.key.startswith(startsw):
            obj = s4.get_object(Bucket='gdelt-all', Key=obj.key)
            df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
            dfa.append(df)

    try:
        data = pd.concat(dfa, axis=0)
        return data
            
    except ValueError:
        print("No data for the dates provided")
        return

def engexport21(df1):
    wsources = list(df1['SOURCEURL'])
    # wsources = random.sample(wsources, int(len(wsources)*0.001))
    data = ''.join(wsources)
    data = data.split("htt")
        # Cleaning

    # Cleaning

    data2 = []

    for line in data:
        line2 = pathlib.PurePath(line).name
        if not re.match(r"^article", line2):
            if not re.match(r'^[0-9].*', line2):
                data2.append(line2)

    clean_txt = []
    for lines in data2:
        desc = lines.lower()

        #remove punctuation
        desc = re.sub('[^a-zA-Z]', ' ', desc)

        #remove tags
        desc=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",desc)

        #remove digits and special chars
        desc=re.sub("(\\d|\\W)+"," ",desc)

        desc=desc.replace("-", ' ')

        desc=desc.replace("html", '')
        desc=desc.replace("<UDIV>", '')
        desc=desc.replace("udiv", '')
        clean_txt.append(desc)    



    for i in clean_txt[:]:
        if len(i) <= 25:
            clean_txt.remove(i)

    data3=[]
    for i in clean_txt:
        data3.append(i.strip())


    # to remove duplicated
    # from list
    def remove_duplicates(l):
        return list(set(l))
    data3 = remove_duplicates(data3)    
    df3 = pd.DataFrame(data3)
    df3.to_csv(r'HeadnewsEngExport.csv', index = None, header=True)
    return data3

#V2-ENGL-GKG FAMILY##########################################################################
    
def enggkg1(x):
    # v2 English-GKG
    dfa = []
    prefix = 'v2/dt=' + x + '/'
    startsw = 'v2/dt=' + x + '/' + x + '-en-gkg'
    for obj in bucket.objects.filter(Prefix=prefix):
        if obj.key.startswith(startsw):
            obj = s4.get_object(Bucket='gdelt-all', Key=obj.key)
            df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
            dfa.append(df)
                    
    try:
        data = pd.concat(dfa, axis=0)
        return data
            
    except ValueError:
        print("No data for the dates provided")
        return

def enggkg21(df1):    
    wsources = list(df1['DocumentIdentifier'])
    # wsources = random.sample(wsources, int(len(wsources)*0.001))
    data = ''.join(wsources)
    data = data.split("htt")
        # Cleaning

    # Cleaning

    data2 = []

    for line in data:
        line2 = pathlib.PurePath(line).name
        if not re.match(r"^article", line2):
            if not re.match(r'^[0-9].*', line2):
                data2.append(line2)

    clean_txt = []
    for lines in data2:
        desc = lines.lower()

        #remove punctuation
        desc = re.sub('[^a-zA-Z]', ' ', desc)

        #remove tags
        desc=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",desc)

        #remove digits and special chars
        desc=re.sub("(\\d|\\W)+"," ",desc)

        desc=desc.replace("-", ' ')

        desc=desc.replace("html", '')
        desc=desc.replace("<UDIV>", '')
        desc=desc.replace("udiv", '')
        clean_txt.append(desc)    



    for i in clean_txt[:]:
        if len(i) <= 25:
            clean_txt.remove(i)

    data3=[]
    for i in clean_txt:
        data3.append(i.strip())


    # to remove duplicated
    # from list
    def remove_duplicates(l):
        return list(set(l))
    data3 = remove_duplicates(data3)    
    df3 = pd.DataFrame(data3)
    df3.to_csv(r'HeadnewsEngGKG.csv', index = None, header=True)
    return data3
    
#V2-ENG-MENT FAMILY##########################################################################    

def engmen1(x):
    # V2 English-Mentions
    dfa = []
    prefix = 'v2/dt=' + x + '/'
    startsw = 'v2/dt=' + x + '/' + x + '-en-mentions'
    for obj in bucket.objects.filter(Prefix=prefix):
        if obj.key.startswith(startsw):
            obj = s4.get_object(Bucket='gdelt-all', Key=obj.key)
            df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
            dfa.append(df)

    try:
        data = pd.concat(dfa, axis=0)
        return data       
    except ValueError:
        print("No data for the dates provided")
        return


def engmen21(df1):    
    wsources = list(df1['MentionIdentifier'])
    # wsources = random.sample(wsources, int(len(wsources)*0.001))
    data = ''.join(wsources)
    data = data.split("htt")
        # Cleaning

    # Cleaning

    data2 = []

    for line in data:
        line2 = pathlib.PurePath(line).name
        if not re.match(r"^article", line2):
            if not re.match(r'^[0-9].*', line2):
                data2.append(line2)

    clean_txt = []
    for lines in data2:
        desc = lines.lower()

        #remove punctuation
        desc = re.sub('[^a-zA-Z]', ' ', desc)

        #remove tags
        desc=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",desc)

        #remove digits and special chars
        desc=re.sub("(\\d|\\W)+"," ",desc)

        desc=desc.replace("-", ' ')

        desc=desc.replace("html", '')
        desc=desc.replace("<UDIV>", '')
        desc=desc.replace("udiv", '')
        clean_txt.append(desc)    



    for i in clean_txt[:]:
        if len(i) <= 25:
            clean_txt.remove(i)

    data3=[]
    for i in clean_txt:
        data3.append(i.strip())


    # to remove duplicated
    # from list
    def remove_duplicates(l):
        return list(set(l))
    data3 = remove_duplicates(data3)    
    df3 = pd.DataFrame(data3)
    df3.to_csv(r'HeadnewsEngMent.csv', index = None, header=True)
    return data3
    
    
#V2-TR-EXP##########################################################################
    
def transl1(x):
    # V2 Translations
    dfa = []
    prefix = 'v2/dt=' + x + '/'
    startsw = 'v2/dt=' + x + '/' + x + '-tr-export'
    for obj in bucket.objects.filter(Prefix=prefix):
        if obj.key.startswith(startsw):
            obj = s4.get_object(Bucket='gdelt-all', Key=obj.key)
            df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
            dfa.append(df)
                    
    try:
        data = pd.concat(dfa, axis=0)
        return data
            
    except ValueError:
        print("No data for the dates provided")
        return

def transl21(df1):
    # Injesting the pandas dataframe
    wsources = list(df1['SOURCEURL'])
    # wsources = random.sample(wsources, int(len(wsources)*0.001))
    data = ''.join(wsources)
    data = data.split("htt")
        # Cleaning

    # Cleaning

    data2 = []

    for line in data:
        line2 = pathlib.PurePath(line).name
        if not re.match(r"^article", line2):
            if not re.match(r'^[0-9].*', line2):
                data2.append(line2)

    clean_txt = []
    for lines in data2:
        desc = lines.lower()

        #remove punctuation
        desc = re.sub('[^a-zA-Z]', ' ', desc)

        #remove tags
        desc=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",desc)

        #remove digits and special chars
        desc=re.sub("(\\d|\\W)+"," ",desc)

        desc=desc.replace("-", ' ')

        desc=desc.replace("html", '')
        desc=desc.replace("<UDIV>", '')
        desc=desc.replace("udiv", '')
        clean_txt.append(desc)    



    for i in clean_txt[:]:
        if len(i) <= 25:
            clean_txt.remove(i)

    data3=[]
    for i in clean_txt:
        data3.append(i.strip())


    # to remove duplicated
    # from list
    def remove_duplicates(l):
        return list(set(l))
    data3 = remove_duplicates(data3)    
    df3 = pd.DataFrame(data3)
    df3.to_csv(r'HeadnewsTransl.csv', index = None, header=True)
    return data3

# INTERFACE APP      
        
def submenu2():

    again = 'y'
    
    # Loop for more GDELT User interaction

    while again.upper() == 'Y':
        
        today = date.today()- timedelta(days=1)
        dt=parse(str(today))
        x=date_string=dt.strftime('%Y%m%d')
        global done
        
        print('APPLICATION MENU')
        print('GDELT metadata for one day events in the world')
        print('News headlines, Wordcloud, LDA-Topics Analysis')
        print('For: ', today)
        
        print(red('Enter 1 for GDELT 1.0 - GKG', ['bold']))
        print(red('Enter 2 for GDELT 1.0 - COUNTS', ['bold']))
        print(blue('Enter 3 for GDELT 2.0 - ENGLISH - EXPORT', ['bold']))
        print(blue('Enter 4 for GDELT 2.0 - ENGLISH - MENTIONS', ['bold']))
        print(blue('Enter 5 for GDELT 2.0 - ENGLISH - GKG', ['bold']))
        print(green('Enter 6 for GDELT 2.0 - TRANSLATIONS - EXPORT', ['bold']))
        
        option = int(input('Which option [1, 2, 3, 4, 5, 6]: '))
        
        if option == 1:
            
            done = False
            t = threading.Thread(target=animate)
            t.start()
            r1=vcounts1(x)
            r2=vcounts21(r1)
            vlda(r2)
            r3=vwordc(r2)
            time.sleep(10)
            done = True           

        elif option == 2:

            done = False
            t = threading.Thread(target=animate)
            t.start()
            r1=vgkg1(x)
            r2=vgkg21(r1)
            vlda(r2)
            r3=vwordc(r2)
            time.sleep(10)
            done = True           

            
        elif option == 3:

            done = False
            t = threading.Thread(target=animate)
            t.start()
            r1=engexport1(x)
            r2=engexport21(r1)
            vlda(r2)
            r3=vwordc(r2)
            time.sleep(10)
            done = True           

            
        elif option == 4:

            done = False
            t = threading.Thread(target=animate)
            t.start()
            r1=enggkg1(x)
            r2=enggkg21(r1)
            vlda(r2)
            r3=vwordc(r2)
            time.sleep(10)
            done = True           


        elif option == 5:

            done = False
            t = threading.Thread(target=animate)
            t.start()
            r1=engmen1(x)
            r2=engmen21(r1)
            vlda(r2)
            r3=vwordc(r2)
            time.sleep(10)
            done = True           

            
        elif option == 6:

            done = False
            t = threading.Thread(target=animate)
            t.start()
            r1=transl1(x)
            r2=transl21(r1)
            vlda(r2)
            r3=vwordc(r2)
            time.sleep(10)
            done = True           

 
        else:
            print('follow the instructions')
            
        again = input('Same app from another stream type (y = YES, n = NO): ')




    
