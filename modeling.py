import numpy as np
import pandas as pd
import prepare as prep
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import explore as ex

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings('ignore')

def modeling_df(df):
    '''
    This function preps the data for modeling
    '''
    df.drop(columns=['id', 'name', 'num_user_ratings', 'average_user_rating', 'num_user_complexity_votes', 
                 'average_learning_complexity', 'average_strategy_complexity', 'year_published'], inplace=True)
    train, val, test=ex.tts(df, stratify='rank')
    return train, val, test

def models(train, val):
    '''
    this function prints results for models
    '''
    x_train=train.drop(columns=['rank'])
    y_train=train['rank']

    x_val=val.drop(columns=['rank'])
    y_val=val['rank']
    
    results=[]
    logit = LogisticRegression(C=.5, random_state=8675309, intercept_scaling=1, solver='lbfgs')
    logit.fit(x_train, y_train)
    in_sample=logit.score(x_train,y_train)
    out_of_sample=logit.score(x_val, y_val)
    output={
        'model': 'LogisticRegression (lbfgs)',
        'train_accuracy': in_sample,
        'validate_accuracy': out_of_sample
    }
    results.append(output)
    
    logit = LogisticRegression(C=1, random_state=8675309, solver='liblinear')
    logit.fit(x_train, y_train)
    in_sample=logit.score(x_train,y_train)
    out_of_sample=logit.score(x_val, y_val)
    output={
        'model': 'LogisticRegression (liblinear)',
        'train_accuracy': in_sample,
        'validate_accuracy': out_of_sample
    }
    results.append(output)
    
    knn= KNeighborsClassifier(n_neighbors=5, weights='uniform')
    knn.fit(x_train,y_train)
    in_sample= knn.score(x_train, y_train)
    out_of_sample= knn.score(x_val, y_val)
    output={
        'model': 'KNeighborsClassifier',
        'train_accuracy': in_sample,
        'validate_accuracy': out_of_sample
    }
    results.append(output)
    
    dtc=DecisionTreeClassifier(max_depth=2, min_samples_leaf=4, random_state=8675309)
    dtc.fit(x_train, y_train)
    in_sample= dtc.score(x_train, y_train)
    out_of_sample= dtc.score(x_val, y_val)
    output={
        'model': 'DecisionTreeClassifier',
        'train_accuracy': in_sample,
        'validate_accuracy': out_of_sample
    }
    results.append(output)
    
    rm= RandomForestClassifier(max_depth= 9, min_samples_leaf= 10, random_state=8675309)
    rm.fit(x_train, y_train)
    in_sample= rm.score(x_train, y_train)
    out_of_sample= rm.score(x_val, y_val)
    output={
        'model': 'RandomForestClassifier',
        'train_accuracy': in_sample,
        'validate_accuracy': out_of_sample
    }
    results.append(output)
    
    results=pd.DataFrame(data=results)
    results['difference']=results['train_accuracy']-results['validate_accuracy'] 
    results=results.sort_values('difference', ascending=False)
    return results