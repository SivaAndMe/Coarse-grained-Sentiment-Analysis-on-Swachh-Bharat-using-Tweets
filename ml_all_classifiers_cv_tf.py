
# all classifiers

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
from sklearn.model_selection import cross_validate,KFold
import datetime
import time
import pandas as pd
#a list of classes
classifiers = [MultinomialNB(),BernoulliNB(),LogisticRegression(),LinearSVC(),AdaBoostClassifier(),RidgeClassifier(),PassiveAggressiveClassifier(),Perceptron()]
clf_names = ['MultinomialNB()','BernoulliNB()','LogisticRegression()','LinearSVC()','AdaBoostClassifier()','RidgeClassifier()','PassiveAggressiveClassifier()','Perceptron()']

for gram in range(1,4):
    i=0

    data=[]
    for clf in classifiers:

        before = datetime.datetime.now()
        before = before.strftime("%H:%M:%S")
        start = time.time()

        cv = CountVectorizer(ngram_range=(1,gram))
        model = make_pipeline(cv,clf)
        model.fit(x_train_copy.values.astype('U'),y_train_copy.values.astype('U'))##
        labels = model.predict(x_val_copy.values.astype('U'))
        ac = accuracy_score(y_val_copy.values.astype('U'),labels)
        kfold = KFold(n_splits=10,shuffle=False,random_state=None)
        results = cross_validate(model,x_train_copy.values.astype('U'),y_train_copy.values.astype('U'),cv=kfold)
        crossval_test_score_mean=results['test_score'].mean()
        crossval_train_score_mean=results['train_score'].mean()
        crossval_test_score_std=results['test_score'].std()
        crossval_train_score_std=results['train_score'].std()
        after = datetime.datetime.now()
        after = after.strftime("%H:%M:%S")
        end = time.time()
        hours = int(after[0:2])-int(before[0:2])
        mins = int(after[3:5])-int(before[3:5])
        secs = int(after[6:8])-int(before[6:8])
        time_taken = str(hours)+":"+str(mins)+":"+str(secs)
        data.append([clf_names[i],ac,crossval_train_score_mean,crossval_test_score_mean,crossval_train_score_std,crossval_test_score_std, end-start])
        i+=1
    d = pd.DataFrame(data,columns=['Classifier','Ac','crossval_train_score_mean','crossval_test_score_mean','crossval_train_score_std','crossval_test_score_std','Time.2'])
    d['Ac_rank'] = d['Ac'].rank(ascending=False)
    d['Time_rank'] = d['Time.2'].rank(ascending=False)
    d['C-rank'] = d['Ac_rank'] + d['Time_rank']
    d['C-rank'] = d['C-rank'].rank(ascending=False)

    print(d)
    gr = str(gram)
    fname = "cv_"+gr+"clfs.csv"
    d.to_csv(fname)
