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
* Conduct an NLP analysis for game desctiptions
* Provide stakeholders with a recipe to create a highly rated board game.


## Executive Summary:
**Insights**
1. one
2. two
3. three


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
       * Do schools with more economically disadvantaged students have a lower average percent passing rate for STAAR exams?
       * Do schools with teachers that have more years of experience have a better average STAAR score passing rates?
       * Of schools with a large proportion of economically disadvantaged students, do the schools with higher average STAAR scores have higher expenses per student?
       * Do schools with above average economically disadvantaged students have significantly higher total expendature per student?
       * Is there a statisticaly significant correlation between the amount of extracurricular expendatures and algebra passing rates?
       * Is there a statisticaly significant correlation between student teacher ratio and all subjects passing rates?
       
* Prep the data for modeling:
    * Split data into X and y train
    * Scale all numeric data excluding target variables:
        * MinMaxScalar() was used to scale data
      
* Develop a model to predict STAAR scores for `english_1`, `english_2`, `algebra`, `biology`, and `history`
   * Regression models were used to predict STAAR scores
       * Linear Regression
       * Lasso Lars
       * Tweedie Regressor
       * Polynomial Regression
   * Evaluate models on train and validate data
   * Select the best model based on the lowest RMSE and difference between in sample and out of sample data RMSE
   * Test the best model on test data
 
* Draw conclusions

## Data Dictionary:


| Feature | Definition |
|:--------|:-----------|
|id| The id number of the school from TEA|
|name| English I, percent of students at approaches grade level or above for English I|
|price| English II, percent of students at approaches grade level or above for English II|
|msrp| Algebra, percent of students at approaches grade level or above for Algebra|
|year_published| Biology, percent of students at approaches grade level or above for Biology|
|min_players| U.S. History, percent of students at approaches grade level or above for U.S. History|
|max_players| EB/EL Current and Monitored, percent of students in the dual-language program that enables emergent bilingual (EB) students/English learners (ELs) to become proficient in listening, speaking, reading, and writing in the English language through the development of literacy and academic skills in the primary language and English.|
|min_playtime| Integer, number of teachers with 0-5 years of experience|
|max_playtime| Integer, number of teachers with 6-10 numbers of experience|
|min_age| Integer, number of teachers with 11 or more years of experience|
|num_user_ratings| The amount of funds (in dollars) spent on extracurriculuars per student|
|average_user_rating| The average total amount of funds (in dollars) spent per student|
|num_user_complexity_votes| students that are from homes that are below the poverty line
|average_learning_complexity| Average Actual Salary, Average amount teachers are being paid in dollars|
|average_strategy_complexity| Percent of teachers with a masters or doctorate degree|
|rank| Count of the number of students per one teacher|
|type| Count of the number of students per one teacher|
|num_distributors| Count of the number of students per one teacher|



## Steps to Reproduce
1. Clone this repo
2. Use the function from acquire.py to acquire the data from the Board Game Atlas API 
3. Use the functions from prepare.py to prepare the data for exploration
4. Run the explore and modeling notebook
5. Run final report notebook
