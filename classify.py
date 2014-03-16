import pickle
import os, sys
import random
import pandas as pd
import numpy as numpy
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelBinarizer, LabelEncoder
from sklearn.cross_validation import cross_val_score, KFold
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression, RidgeClassifierCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import  LinearSVC
from sklearn.externals import joblib
from gettweets import gettweets
from collections import Counter



class TwitterUserInterest():
  
  # uses pipline to transform the data  
  def __init__(self):
    self._pipeline = Pipeline([
                            ('vectorizer',  CountVectorizer(decode_error='ignore', binary=False)),
                            ('tfidf', TfidfTransformer(norm='l1')),
                        ])

  def fit_transform(self, X):
    dataset = self._pipeline.fit_transform(X)
    return dataset

  def transform(self, dataset):
    dataset = self._pipeline.transform(dataset)
    return dataset

   
   

# Trains and returns 3 models
def train_model(X, Y):
    print "Training LR..."
    modelLR = LogisticRegression(penalty='l1', C=100, tol=1e-10)
    modelLR.fit(X.toarray(), Y)
    
    print "Training RC..."
    modelRC = RidgeClassifierCV(alphas=[ 0.1, 1., 10. ])
    modelRC.fit(X.toarray(), Y)
    
    print "Training GBC..."
    modelGBC = GradientBoostingClassifier(subsample=0.5, max_depth=6, n_estimators=50)
    modelGBC.fit(X.toarray(), Y)

    
    return modelGBC, modelRC, modelLR
       


# Main function takes username as parameter
def main(username):
    datadir = "data/"
    labelEncoder = LabelEncoder() 
    df = pd.DataFrame()
    tui = TwitterUserInterest()
    hasModel = False
    modelDir = 'model/'
    #try to load model from the file
    try:
        with open(modelDir + 'twitterGBC.pkl') as m:
            modelGBC = pickle.load(m)
        with open(modelDir + 'twitterRC.pkl') as m:
            modelRC = pickle.load(m)
        with open(modelDir + 'twitterLR.pkl') as m:
            modelLR = pickle.load(m) 
            
        with open(modelDir + 'pipeline.pkl') as p:
            tui._pipeline = pickle.load(p)
        with open(modelDir + 'labelEncoder.pkl') as l:
            labelEncoder = pickle.load(l)

        hasModel = True
    except:
        print "Model not found, creating new model..."
        
        
    if not hasModel:
        #read all the tweet files
        print "Reading tweet files..."
        for file in os.listdir(datadir):
            data = pd.read_csv(datadir + file, names=['tweet','screen','interest'], sep=',', skiprows=1)
            df = df.append(pd.DataFrame({'tweet': data.tweet, 'interest': data.interest, 'index': file}))
            
        
        print "Preparing data..." 
        X = tui.fit_transform(df.tweet)
        Y = labelEncoder.fit_transform(df.interest)
    
      
        #randomize the df array
        numpy.random.seed(0)
        idx = numpy.random.permutation(Y.size)
        X = X[idx]
        Y = Y[idx]
      
      
      
        print "Training Model..."
        modelGBC, modelRC, modelLR = train_model(X, Y)
        

        print "Saving model to the file..."        
        #save model to a file
        #joblib.dump(model, 'twitter.pkl', compress=0)
        with open(modelDir + 'twitterGBC.pkl', 'w') as m:
            pickle.dump(modelGBC, m)
        with open(modelDir + 'twitterRC.pkl', 'w') as m:
            pickle.dump(modelRC, m)
        with open(modelDir + 'twitterLR.pkl', 'w') as m:
            pickle.dump(modelLR, m)
            
        with open(modelDir + 'pipeline.pkl', 'w') as p:
            pickle.dump(tui._pipeline, p) 
        with open(modelDir + 'labelEncoder.pkl', 'w') as l:
            pickle.dump(labelEncoder, l)
         
               
        #print "Cross Validating..."
        #print cross_val_score(model, X.toarray(), Y)


        
    gettweets(screen_name = username, directory = 'test')
    print "Classifying User " + username
    test = pd.read_csv('test/'+username, names=['tweet','screen','interest'], sep=',')   
    
    
    #if we want to classify user in 1 category
    #testtweets = ''
    #for tweet in test.tweet:
    #    testtweets += tweet 
    #X_test = tui.transform([testtweets])

    X_test = tui.transform(test.tweet)
    classificationLR = modelLR.predict(X_test.toarray())
    classificationRC = modelRC.predict(X_test.toarray())
    classificationGBC = modelGBC.predict(X_test.toarray())
    
    interestsLR = labelEncoder.inverse_transform(classificationLR)
    interestsRC = labelEncoder.inverse_transform(classificationRC)
    interestsGBC = labelEncoder.inverse_transform(classificationGBC)
    #print interests
    
    
    #get top 3 interests
    cnt = Counter()
    for interest in [interestsGBC, interestsLR, interestsRC]:
        for word in interest:
            cnt[word] += 1      
          

    print '==========================='
    for interest in cnt.most_common(3):
        print interest[0]




if __name__ == '__main__':
    main(sys.argv[1])
    #python classify.py wsj

    