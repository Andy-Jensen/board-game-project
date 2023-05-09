import numpy as np
import pandas as pd
import prepare as prep
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn.model_selection import train_test_split



def tts(df, stratify=None):
    '''
    removing your test data from the data
    '''
    train_validate, test=train_test_split(df, 
                                 train_size=.9, 
                                 random_state=8675309,
                                 stratify=None)
    '''
    splitting the remaining data into the train and validate groups
    '''            
    train, validate =train_test_split(train_validate, 
                                      test_size=.2, 
                                      random_state=8675309,
                                      stratify=None)
    return train, validate, test


def explore_data():
    df=prep.explore_df()
    for i, r in df.iterrows():
        if r['rank'] <= 100:
            df.loc[i, 'rank'] = 1
        else:
            df.loc[i, 'rank'] = 0
    for i, t in df.iterrows():
        if t['type'] == 'game':
            df.loc[i, 'type'] = 0
        elif t['type'] == 'expansion':
            df.loc[i, 'type'] = 1
        else:
            df.loc[i, 'type'] = 2
    return df


def q9_statistic(train):
    '''
    this function gives the test statistic for question 9
    '''
    alpha=.05
    hirank=train[train['rank']==1]['num_distributors']
    lowrank=train[train['rank']==0]['num_distributors']
    t, p= stats.ttest_ind(hirank, lowrank, alternative='greater')
    if p< alpha:
        print(f'The p-value ({p}) is lower than the alpha ({alpha}) so we reject the null hypothesis.')
    else:
        print('We do not reject the null hypothesis.')


def q9_plots(train):
    '''
    This function plots the necessary plots to visualize explore question 9
    '''
    high=train[train['rank']==1]
    low=train[train['rank']==0]
    plt.figure(figsize=(10,5))
    plt.subplot(221)
    sns.histplot(x='num_distributors', data=high)
    plt.title('High Rated Games')
    plt.xlabel('Number of Distributors')
    plt.ylabel('Number of Games')
    plt.grid(True, alpha=0.3, linestyle='--', axis='y')

    plt.subplot(222)
    sns.histplot(x='num_distributors', data=low)
    plt.title('Low Rated Games')
    plt.xlabel('Number of Distributors')
    plt.ylabel('Number of Games')
    plt.grid(True, alpha=0.3, linestyle='--', axis='y')
    
    plt.figure(figsize=(25,10))
    plt.subplot(223)
    plt.title('All Games')
    sns.histplot(x='num_distributors', data=high, alpha=.7, color='green', label= 'High Rated')
    sns.histplot(x='num_distributors', data=low, alpha=.5, label='Low Rated')
    plt.xlabel('Number of Distributors')
    plt.ylabel('Number of Games')
    plt.axvline(x=(high['num_distributors'].mean()), color='red', label='High Rated Games Mean')
    plt.axvline(x=(low['num_distributors'].mean()), color='yellow', label='Low Rated Games Mean')
    plt.legend()
    plt.grid(True, alpha=0.3, linestyle='--', axis='y')
    plt.subplots_adjust(left=0.1,
                            bottom=-0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.4,
                            hspace=0.4)
    plt.show()