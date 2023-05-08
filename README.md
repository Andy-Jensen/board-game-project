# The Ideal Board Game
<a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-013243.svg?logo=python&logoColor=blue"></a>
<a href="#"><img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="NumPy" src="https://img.shields.io/badge/Numpy-2a4d69.svg?logo=numpy&logoColor=grey"></a>
<a href="#"><img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-8DF9C1.svg?logo=matplotlib&logoColor=blue"></a>
<a href="#"><img alt="seaborn" src="https://img.shields.io/badge/seaborn-65A9A8.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="sklearn" src="https://img.shields.io/badge/sklearn-4b86b4.svg?logo=scikitlearn&logoColor=grey"></a>
<a href="#"><img alt="SciPy" src="https://img.shields.io/badge/SciPy-1560bd.svg?logo=scipy&logoColor=blue"></a>
<a href="#"><img alt="XGBoost" src="https://img.shields.io/badge/XGBoost-1560bd.svg?logo=xgboost&logoColor=blue"></a>


## Project Description:
Board games are loved by everyone, young and old. They are something that brings people together for countless hours of social lesiure. The only thing better than the time spent with friends and family is enjoying the game you are playing while doing it. With so many choices and competition in the industry, how can a company produce an enjoyable game and become a favorite of those who play it? The board game industry has produced such games before, but what if there was a recipe for creating a board game that people will love? In 2022 the board game market was worth about $3.13 billion. With that much money being spent for board games, I will be using data to see if there is a popular commonality among highly rated board games and develop a recipe of features to build the next top rated board game.

## Project Goals:
* Identify drivers of highly rated board games
* Build a model to accurately predict if a board game will have achieve a high rating.
* Conduct an NLP analysis for game descriptions and mechanics
* Provide stakeholders with a recipe to create a highly rated board game.


## Executive Summary:
1. There were no features found that indicate if a board game would rank high (top 10%) other than number of distributors.
2. There were some mechanics in the top 10% of board games that are not in the top mechanics of other board games.
3. The Descriptions of the games indicate that there may be a certain set of elements in a board game that are more popular.


## Initial Hypothesis:
I have a few thoughts about what I may find before I explore the data in earnest. I think that the more complex a game is, the more average it will be. There will always be a population that likes complex games, but conversly the most popular games I think would be of average complexity. This would hold the interest of both people that like complex games and those that don't want to read the rule book for 2 hours before play starts. I also think there will be more popular genres than others. With the rise of fantasy genres I expect to see those at the top. I am not sure how publishing date will factor in. Regardless if a game is newer or older if it's good, it's good. I think there will be a good mix of more recently published popular games and also "old" popular games because they have been around for such a long time.

## Project Plan:

* Acquire the data:
  * An API for Board Game Atlas was used to acquire the data
      * https://www.boardgameatlas.com/api/docs

* Data prep for exploration:
    * The inital data had 84 columns and 1000 rows
        * The shape of the data has been reduced to 18 columns and 995 rows
    * Nulls were removed/encoded:
        * There were not a lot of nulls so the information was encoded after looking up the information online
        * There were a few entries that had nulls that spanned across multiple features and those specific entries were dropped
        
* Separate into train, validate, and test datasets
 
* Explore data to develop an understanding of what features affect a board games rating.
   * Initial questions:
       * Which mechanics are most utalized by all board games?
       * Do higher rated games have any features that are significantly different than games that are not higher rated?
           * Statistical tests were run for each feature
       * Explore the bigrams and trigrams of the top 10% of board games description and the rest of the board games.
       
* Prep the data for modeling:
    * Split data into X and y train
    * Scale all numeric data excluding target variables:
        * MinMaxScalar() was used to scale data
      
* Develop a model to predict if a board game will rank in the top 10% or not
   * Classification models will be used to predict rank
       * Decision Tree
       * Random Forest
       * KNN
       * 
   * Evaluate models on train and validate data
   * Select the best model based on accuracy
   * Test the best model on test data
 
* Draw conclusions

## Data Dictionary:


| Feature | Definition |
|:--------|:-----------|
|id| The id number of the game|
|name| The name of the game|
|price| The lowest current available price for the game|
|msrp| Manufacturer suggested retail price|
|year_published| The year the game was made|
|min_players| Minimum number of players required to play the game|
|max_players| The maximum number of players that can play the game|
|min_playtime| The manufacturers estimated minimum time to play the game|
|max_playtime| The manufacturers estimated maximum time to play the game|
|min_age| The recommended minimum age required to play the game|
|num_user_ratings| The number of user ratings the game has recieved on boardgameatlas|
|average_user_rating| The average rating (1-5) the game has recieved from the users|
|num_user_complexity_votes| The average rating (1-5) of the games complexity as rated by the users|
|average_learning_complexity| The average rating (1-5) of the games learning complexity as rated by the users|
|average_strategy_complexity| PThe average rating (1-5) of the games strategy complexity as rated by the users|
|rank| The rank of the game|
|type| Either 'game', 'expansion', or 'accessory' indicating the type of product|
|num_distributors| The number of distributors of the game|



## Steps to Reproduce
1. Clone this repo
2. Use the function from acquire.py to acquire the data from the Board Game Atlas API 
3. Use the functions from prepare.py to prepare the data for exploration
4. Run the explore and modeling notebook
5. Run final report notebook
