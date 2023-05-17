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

def get_baseline(train):
    '''
    this will give the baseline for the model to beat
    '''
    train['baseline']=0
    y_train=train['rank']
    baseline = accuracy_score(y_train, train['baseline'])
    train.drop(columns='baseline', inplace=True)
    return print(f'The baseline our model needs to beat is: {round(baseline,4)*100}%')

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


def modeling_viz(train, val, test):
    '''
    this function will give the visualization for the models
    '''
    x_train=train.drop(columns=['rank'])
    y_train=train['rank']

    x_val=val.drop(columns=['rank'])
    y_val=val['rank']

    x_test=test.drop(columns=['rank'])
    y_test=test['rank']

    rm= RandomForestClassifier(max_depth= 9, min_samples_leaf= 10, random_state=8675309)
    rm.fit(x_train, y_train)
    trainacc = rm.score(x_train,y_train)
    valacc = rm.score(x_val, y_val)
    testacc=rm.score(x_test, y_test)

    plt.figure(figsize=(7,7))
    X = ['Random Forest']
    train['baseline']=0
    baseline=accuracy_score(y_train, train['baseline'])

    X_axis = np.arange(len(X))

    plt.bar(X_axis[0] - 0.2, trainacc, 0.2, label = 'Train Accuracy', color=['blue'], ec='black')
    plt.bar(X_axis[0] + 0.0, valacc, 0.2, label = 'Validate Accuracy', color=['green'], ec='black')
    plt.bar(X_axis[0] + 0.2, testacc, 0.2, label = 'Test Accuracy', color=['rebeccapurple'], ec='black')


    plt.axhline(y = baseline, color = 'r', linestyle = '-', label='Baseline Accuracy')

    plt.xticks(X_axis, X)
    plt.xlabel("Model")
    plt.ylabel("Accuracy")
    plt.title("Accuracy of Model vs Baseline")
    plt.ylim(0, 1.2)
    plt.grid(True, alpha=0.3, linestyle='--', axis='y')
    plt.legend()
    plt.show()