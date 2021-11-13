import pickle
import re

import pandas as pd

from sklearn.model_selection import train_test_split    
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from collections import Counter 

def ngram(token, n):
    output= []
    for i in range(n-1, len(token)):
        ngram = ' '.join(token[i-n+1:i+1])
        output.append(ngram)
    return output

def create_feature(text, nrange=(1,1)):
    text_features=[]
    text = text.lower()
    text_alphanum = re.sub('[^a-z0-9]')
    for n in range(nrange[0], nrange[1]+1):
        text_features += ngram(text_alphanum.split(), n)
    text_punc = re.sub('[a-z0-9]', ' ' , text)
    text_features += ngram(text_punc.split(), 1)
    return Counter(text_features)

def train(clf, x, y):
    clf.fit(x,y)
    return clf

df = pd.read_csv("./data/tweet_emotions.csv")           
df = df.drop(["tweet_id"], axis=1)
df = list(df.to_records(index=False))                   

X = []
y = []
for label, text in df:
    y.append(label)                                     
    X.append(create_feature(text, nrange=(1,4)))       
   
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle = True, random_state=1)    
vectorizer = DictVectorizer(sparse=True)               
X_train = vectorizer.fit_transform(X_train)             

with open("dict.pickle", "wb") as b:
    pickle.dump(vectorizer, b)

X_test = vectorizer.transform(X_test)                   
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)              

with open("rfc.pickle" , "wb") as f: 
    pickle.dump(rfc, f)

svc = SVC(probability=True)
svc.fit(X_train, y_train)

with open("svc.pickle", "wb") as f:
    pickle.dump(svc, f)

linearSVC = LinearSVC()
linearSVC.fit(X_train, y_train)

with open("lsvc.pickle", "wb") as f:
    pickle.dump(linearSVC, f)

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

with open("dtc.pickle", "wb") as f:
    pickle.dump(dtc, f)

print("Training done.")
