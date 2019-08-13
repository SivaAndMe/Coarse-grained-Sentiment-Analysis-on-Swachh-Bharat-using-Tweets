
from sklearn.svm import LinearSVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score,precision_score,recall_score
import datetime
import time
import pandas as pd

classifiers = [BernoulliNB(),LogisticRegression(),LinearSVC(),AdaBoostClassifier(),RidgeClassifier(),PassiveAggressiveClassifier(),Perceptron()]
clf_names = ['BernoulliNB()','LogisticRegression()','LinearSVC()','AdaBoostClassifier()','RidgeClassifier()','PassiveAggressiveClassifier()','Perceptron()']
gensim_names = ['DBOW','DMC','DMM','DBOW+DMM','DBOW+DMC']
data=[]
j=0
for train_vecs,val_vecs in vecs:
    i=0
    for clf in classifiers:

        before = datetime.datetime.now()
        before = before.strftime("%H:%M:%S")
        start = time.time()


        clf.fit(train_vecs,y_train)
        ac = clf.score(val_vecs,y_val)

        after = datetime.datetime.now()
        after = after.strftime("%H:%M:%S")
        end = time.time()
        hours = int(after[0:2])-int(before[0:2])
        mins = int(after[3:5])-int(before[3:5])
        secs = int(after[6:8])-int(before[6:8])
        time_taken = str(hours)+":"+str(mins)+":"+str(secs)
        data.append([gensim_names[j],clf_names[i],ac,end-start])
        i+=1
    j+=1
d = pd.DataFrame(data,columns=['Model','Classifier','Ac','Time'])
#     d['Ac_rank'] = d['Ac'].rank(ascending=False)
#     d['Time_rank'] = d['Time.2'].rank(ascending=False)
#     d['C-rank'] = d['Ac_rank'] + d['Time_rank']
#     d['C-rank'] = d['C-rank'].rank(ascending=False)

print(d)
d.to_csv('gensim_all_clfs.csv')
