import numpy as np
import pandas as pd
import prepare as prep
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn.model_selection import train_test_split
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import unicodedata
import re



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



def top_mech_plt():
    '''
    shows a plot of top games' mechanics
    '''
    top=pd.read_csv('top_100_mechanics.csv')
    top=pd.DataFrame(top.value_counts()).head(20).reset_index().rename(columns={0: 'num_games'})
    plt.barh(y='mechanics',width='num_games', data=top)
    plt.title('Top Mechanics of High Rated Games')
    plt.xlabel('Number of Games')
    plt.ylabel('Mechanic')
    plt.grid(True, alpha=0.3, linestyle='--', axis='x')
    plt.show()

def low_mech_plt():
    '''
    shows a plot of lower games' mechanics
    '''
    low=pd.read_csv('over_100_mechanics.csv')
    low=pd.DataFrame(low.value_counts()).head(20).reset_index().rename(columns={0: 'num_games'})
    plt.barh(y='mechanics',width='num_games', data=low)
    plt.title('Top Mechanics of Lower Rated Games')
    plt.xlabel('Number of Games')
    plt.ylabel('Mechanic')
    plt.grid(True, alpha=0.3, linestyle='--', axis='x')
    plt.show()

def top_mechanics():
    '''
    this function will take all mechanics from all games and show the top 20
    '''
    m=pd.read_csv('mechanic_df')
    return m.value_counts().head(20)

def compare_descriptions():
    '''
    this will get the descriptions and separate them into high and low then show the top bigrams and trigrams of 
    all high and low rated boardgames
    '''
    df=pd.read_csv('descriptions.csv')
    des = df['description_preview']
    tokenizer = nltk.tokenize.ToktokTokenizer()
    ps = nltk.porter.PorterStemmer()
    stopword_list = stopwords.words('english')
    new_stopwords = ['game', 'card', 'player', 'board', 'year', 'jahr']
    stopword_list.extend(new_stopwords)
    high_des=[]
    low_des=[]
    for d in range(0, 978):
        des[d]=des[d].lower()
        des[d] = unicodedata.normalize('NFKD', des[d]).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        des[d] = re.sub(r"[^a-z0-9'\s-]", '', des[d])
        des[d]=tokenizer.tokenize(des[d], return_str=True)
        stems=[ps.stem(word) for word in des[d].split()]
        des[d] = ' '.join(stems)
        words = des[d].split()
        filtered_words = [w for w in words if w not in stopword_list]
        des[d] = ' '.join(filtered_words)
    for i, r in df.iterrows():
        if r['rank'] <= 100:
            df.loc[i, 'rank'] = 1
        else:
            df.loc[i, 'rank'] = 0
    for d in range(0,103):
        high_des.append(des[d])
    high_des=",".join(high_des)
    high_des=high_des.replace(',', ' ')
    high_des=high_des.replace('\'', '')
    high_des=high_des.replace('  ', ' ')
    low=df[df['rank']==0]['description_preview']
    for d in range(103,876):
        low_des.append(low[d])
    low_des.pop(249)
    low_des=",".join(low_des)
    low_des=low_des.replace(',', ' ')
    low_des=low_des.replace('\'', '')
    low_des=low_des.replace('  ', ' ')
    top_20_high_bigrams = (pd.Series(nltk.ngrams(high_des.split(), 2))
                      .value_counts()
                      .head(20))
    top_20_low_bigrams = (pd.Series(nltk.ngrams(low_des.split(), 2))
                      .value_counts()
                      .head(20))
    top_20_high_trigrams = (pd.Series(nltk.ngrams(high_des.split(), 3))
                      .value_counts()
                      .head(20))
    top_20_low_trigrams = (pd.Series(nltk.ngrams(low_des.split(), 3))
                      .value_counts()
                      .head(20))

    print('High rated games\' bigrams:\n', top_20_high_bigrams.head(), '\n\nLow rated games\' bigrams:\n',
         top_20_low_bigrams.head(), '\n\nHigh rated games\' trigrams:\n', top_20_high_trigrams.head(),
         '\n\nLow rated games\' trigrams:\n', top_20_low_trigrams.head())


def low_bigrams():
    '''
    this will plot the lower rated bigrams
    '''
    df=pd.read_csv('descriptions.csv')
    des = df['description_preview']
    tokenizer = nltk.tokenize.ToktokTokenizer()
    ps = nltk.porter.PorterStemmer()
    stopword_list = stopwords.words('english')
    new_stopwords = ['game', 'card', 'player', 'board', 'year', 'jahr']
    stopword_list.extend(new_stopwords)
    high_des=[]
    low_des=[]
    for d in range(0, 978):
        des[d]=des[d].lower()
        des[d] = unicodedata.normalize('NFKD', des[d]).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        des[d] = re.sub(r"[^a-z0-9'\s-]", '', des[d])
        des[d]=tokenizer.tokenize(des[d], return_str=True)
        stems=[ps.stem(word) for word in des[d].split()]
        des[d] = ' '.join(stems)
        words = des[d].split()
        filtered_words = [w for w in words if w not in stopword_list]
        des[d] = ' '.join(filtered_words)
    for i, r in df.iterrows():
        if r['rank'] <= 100:
            df.loc[i, 'rank'] = 1
        else:
            df.loc[i, 'rank'] = 0
    for d in range(0,103):
        high_des.append(des[d])
    high_des=",".join(high_des)
    high_des=high_des.replace(',', ' ')
    high_des=high_des.replace('\'', '')
    high_des=high_des.replace('  ', ' ')
    low=df[df['rank']==0]['description_preview']
    for d in range(103,876):
        low_des.append(low[d])
    low_des.pop(249)
    low_des=",".join(low_des)
    low_des=low_des.replace(',', ' ')
    low_des=low_des.replace('\'', '')
    low_des=low_des.replace('  ', ' ')
    top_20_high_bigrams = (pd.Series(nltk.ngrams(high_des.split(), 2))
                      .value_counts()
                      .head(20))
    top_20_low_bigrams = (pd.Series(nltk.ngrams(low_des.split(), 2))
                      .value_counts()
                      .head(20))
    top_20_high_trigrams = (pd.Series(nltk.ngrams(high_des.split(), 3))
                      .value_counts()
                      .head(20))
    top_20_low_trigrams = (pd.Series(nltk.ngrams(low_des.split(), 3))
                      .value_counts()
                      .head(20))

    low_bigram_viz=top_20_low_bigrams
    low_bigram_viz.plot.barh()
    plt.grid(axis='x', alpha=.5, ls='--')
    plt.title('Top Bigrams of Lower Rated Games')
    plt.xlabel('Count')
    plt.ylabel('Bigrams')
    plt.show()


def high_bigrams():
    '''
    this will plot the top 20 higher rated bigrams
    '''
    df=pd.read_csv('descriptions.csv')
    des = df['description_preview']
    tokenizer = nltk.tokenize.ToktokTokenizer()
    ps = nltk.porter.PorterStemmer()
    stopword_list = stopwords.words('english')
    new_stopwords = ['game', 'card', 'player', 'board', 'year', 'jahr']
    stopword_list.extend(new_stopwords)
    high_des=[]
    low_des=[]
    for d in range(0, 978):
        des[d]=des[d].lower()
        des[d] = unicodedata.normalize('NFKD', des[d]).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        des[d] = re.sub(r"[^a-z0-9'\s-]", '', des[d])
        des[d]=tokenizer.tokenize(des[d], return_str=True)
        stems=[ps.stem(word) for word in des[d].split()]
        des[d] = ' '.join(stems)
        words = des[d].split()
        filtered_words = [w for w in words if w not in stopword_list]
        des[d] = ' '.join(filtered_words)
    for i, r in df.iterrows():
        if r['rank'] <= 100:
            df.loc[i, 'rank'] = 1
        else:
            df.loc[i, 'rank'] = 0
    for d in range(0,103):
        high_des.append(des[d])
    high_des=",".join(high_des)
    high_des=high_des.replace(',', ' ')
    high_des=high_des.replace('\'', '')
    high_des=high_des.replace('  ', ' ')
    low=df[df['rank']==0]['description_preview']
    for d in range(103,876):
        low_des.append(low[d])
    low_des.pop(249)
    low_des=",".join(low_des)
    low_des=low_des.replace(',', ' ')
    low_des=low_des.replace('\'', '')
    low_des=low_des.replace('  ', ' ')
    top_20_high_bigrams = (pd.Series(nltk.ngrams(high_des.split(), 2))
                      .value_counts()
                      .head(20))
    top_20_low_bigrams = (pd.Series(nltk.ngrams(low_des.split(), 2))
                      .value_counts()
                      .head(20))
    top_20_high_trigrams = (pd.Series(nltk.ngrams(high_des.split(), 3))
                      .value_counts()
                      .head(20))
    top_20_low_trigrams = (pd.Series(nltk.ngrams(low_des.split(), 3))
                      .value_counts()
                      .head(20))

    low_bigram_viz=top_20_high_bigrams
    low_bigram_viz.plot.barh()
    plt.grid(axis='x', alpha=.5, ls='--')
    plt.title('Top Bigrams of High Rated Games')
    plt.xlabel('Count')
    plt.ylabel('Bigrams')
    plt.show()

def high_trigrams():
    '''
    this will plot the top 20 higher rated trigrams
    '''
    df=pd.read_csv('descriptions.csv')
    des = df['description_preview']
    tokenizer = nltk.tokenize.ToktokTokenizer()
    ps = nltk.porter.PorterStemmer()
    stopword_list = stopwords.words('english')
    new_stopwords = ['game', 'card', 'player', 'board', 'year', 'jahr']
    stopword_list.extend(new_stopwords)
    high_des=[]
    low_des=[]
    for d in range(0, 978):
        des[d]=des[d].lower()
        des[d] = unicodedata.normalize('NFKD', des[d]).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        des[d] = re.sub(r"[^a-z0-9'\s-]", '', des[d])
        des[d]=tokenizer.tokenize(des[d], return_str=True)
        stems=[ps.stem(word) for word in des[d].split()]
        des[d] = ' '.join(stems)
        words = des[d].split()
        filtered_words = [w for w in words if w not in stopword_list]
        des[d] = ' '.join(filtered_words)
    for i, r in df.iterrows():
        if r['rank'] <= 100:
            df.loc[i, 'rank'] = 1
        else:
            df.loc[i, 'rank'] = 0
    for d in range(0,103):
        high_des.append(des[d])
    high_des=",".join(high_des)
    high_des=high_des.replace(',', ' ')
    high_des=high_des.replace('\'', '')
    high_des=high_des.replace('  ', ' ')
    low=df[df['rank']==0]['description_preview']
    for d in range(103,876):
        low_des.append(low[d])
    low_des.pop(249)
    low_des=",".join(low_des)
    low_des=low_des.replace(',', ' ')
    low_des=low_des.replace('\'', '')
    low_des=low_des.replace('  ', ' ')
    top_20_high_bigrams = (pd.Series(nltk.ngrams(high_des.split(), 2))
                      .value_counts()
                      .head(20))
    top_20_low_bigrams = (pd.Series(nltk.ngrams(low_des.split(), 2))
                      .value_counts()
                      .head(20))
    top_20_high_trigrams = (pd.Series(nltk.ngrams(high_des.split(), 3))
                      .value_counts()
                      .head(20))
    top_20_low_trigrams = (pd.Series(nltk.ngrams(low_des.split(), 3))
                      .value_counts()
                      .head(20))

    low_bigram_viz=top_20_high_trigrams
    low_bigram_viz.plot.barh()
    plt.grid(axis='x', alpha=.5, ls='--')
    plt.title('Top Trigrams of High Rated Games')
    plt.xlabel('Count')
    plt.ylabel('Trigrams')
    plt.show()

def low_trigrams():
    '''
    this will plot the top 20 lower rated trigrams
    '''
    df=pd.read_csv('descriptions.csv')
    des = df['description_preview']
    tokenizer = nltk.tokenize.ToktokTokenizer()
    ps = nltk.porter.PorterStemmer()
    stopword_list = stopwords.words('english')
    new_stopwords = ['game', 'card', 'player', 'board', 'year', 'jahr']
    stopword_list.extend(new_stopwords)
    high_des=[]
    low_des=[]
    for d in range(0, 978):
        des[d]=des[d].lower()
        des[d] = unicodedata.normalize('NFKD', des[d]).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        des[d] = re.sub(r"[^a-z0-9'\s-]", '', des[d])
        des[d]=tokenizer.tokenize(des[d], return_str=True)
        stems=[ps.stem(word) for word in des[d].split()]
        des[d] = ' '.join(stems)
        words = des[d].split()
        filtered_words = [w for w in words if w not in stopword_list]
        des[d] = ' '.join(filtered_words)
    for i, r in df.iterrows():
        if r['rank'] <= 100:
            df.loc[i, 'rank'] = 1
        else:
            df.loc[i, 'rank'] = 0
    for d in range(0,103):
        high_des.append(des[d])
    high_des=",".join(high_des)
    high_des=high_des.replace(',', ' ')
    high_des=high_des.replace('\'', '')
    high_des=high_des.replace('  ', ' ')
    low=df[df['rank']==0]['description_preview']
    for d in range(103,876):
        low_des.append(low[d])
    low_des.pop(249)
    low_des=",".join(low_des)
    low_des=low_des.replace(',', ' ')
    low_des=low_des.replace('\'', '')
    low_des=low_des.replace('  ', ' ')
    top_20_high_bigrams = (pd.Series(nltk.ngrams(high_des.split(), 2))
                      .value_counts()
                      .head(20))
    top_20_low_bigrams = (pd.Series(nltk.ngrams(low_des.split(), 2))
                      .value_counts()
                      .head(20))
    top_20_high_trigrams = (pd.Series(nltk.ngrams(high_des.split(), 3))
                      .value_counts()
                      .head(20))
    top_20_low_trigrams = (pd.Series(nltk.ngrams(low_des.split(), 3))
                      .value_counts()
                      .head(20))

    low_bigram_viz=top_20_low_trigrams
    low_bigram_viz.plot.barh()
    plt.grid(axis='x', alpha=.5, ls='--')
    plt.title('Top Trigrams of Lower Rated Games')
    plt.xlabel('Count')
    plt.ylabel('Trigrams')
    plt.show()