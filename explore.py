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
