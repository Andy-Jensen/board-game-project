import numpy as np
import pandas as pd
import env
import requests
import time

def get_games(num=100, pages=1):
    '''
    This function will get any 100 entries from the api
    '''
    limit=num
    for n in range(pages+1):
        pages=n*num
        url=f'https://api.boardgameatlas.com/api/search?limit={limit}&skip={pages}&pretty=true&client_id={env.key}'
        response = requests.get(url)
        data=response.json()
    games=pd.DataFrame(data['games'])
    return games

def all_games():
    '''
    This will get 1000 board game entries from the api and save it to a csv
    '''
    a=get_games(num=100, pages=0)
    b=get_games(num=100, pages=1)
    c=get_games(num=100, pages=2)
    d=get_games(num=100, pages=3)
    e=get_games(num=100, pages=4)
    f=get_games(num=100, pages=5)
    g=get_games(num=100, pages=6)
    h=get_games(num=100, pages=7)
    i=get_games(num=100, pages=8)
    j=get_games(num=100, pages=9)
    df=pd.concat([a, b, c, d, e, f, g, h, i, j], ignore_index=True)
    df.to_csv('games.csv')
    return df

def get_games_mech(num=100, pages=1):
    '''
    This will get the entries for any single page and not convert to a dataframe. Used in getting a list of all mechanics
    '''
    limit=num
    for n in range(pages+1):
        pages=n*num
        url=f'https://api.boardgameatlas.com/api/search?limit={limit}&skip={pages}&pretty=true&client_id={env.key}'
        response = requests.get(url)
        data=response.json()
    return data

def all_games_mech():
    '''
    gets all entries in json format
    '''
    a=get_games_mech(num=100, pages=0)
    time.sleep(5)
    b=get_games_mech(num=100, pages=1)
    time.sleep(5)
    c=get_games_mech(num=100, pages=2)
    time.sleep(5)
    d=get_games_mech(num=100, pages=3)
    time.sleep(5)
    e=get_games_mech(num=100, pages=4)
    time.sleep(5)
    f=get_games_mech(num=100, pages=5)
    time.sleep(5)
    g=get_games_mech(num=100, pages=6)
    time.sleep(5)
    h=get_games_mech(num=100, pages=7)
    time.sleep(5)
    i=get_games_mech(num=100, pages=8)
    time.sleep(5)
    j=get_games_mech(num=100, pages=9)
    return a, b, c, d, e, f, g, h, i, j

def mechanics_key():
    '''
    this function gets the name of all the mechanics from the api
    '''
    url=f'https://api.boardgameatlas.com/api/game/mechanics?client_id={env.key}'
    response=requests.get(url)
    data=response.json()
    mech=data['mechanics']
    new_mech={}
    for d in mech:
        new_mech[d['id']]=d['name']
    return new_mech

def all_mechanics():
    '''
    returns all the mechanics of all games in a dataframe and saves a list of all the mechanics to a csv
    '''
    a, b, c, d, e, f, g, h, i, j=all_games_mech()
    key=mechanics_key()
    games=[a, b, c, d, e, f, g, h, i, j]
    game_mechanics=[]
    for g in games:
        game_mechanics.extend(get_mechanics(g))
    series=pd.Series(game_mechanics).map(key)
    df=pd.DataFrame(mechtest, columns=['mechanics'])
    df.to_csv('mechanic_df', index=False)
    return df
    