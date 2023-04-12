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

* **Acquire the data:
  * Web scraping was used to acquire the data
  * The data is from Texas Education Agency (TEA).

* **Data prep for exploration:**
    * Schools that had special characters were removed from analysis
        * special characters (`*`, `-`, `?`, n/a)
    * Nulls were removed:
        * Nulls or reserved information was incoded into the special characters above and removed
    * All the percent signs, dollar signs, and commas were removed from values
    * Columns were combined into desired features
        * `high_edu` was generated from combining percent of teachers that have a masters or doctorate
        * Features for `teacher_exp_0to5`, `teacher_exp_6to10`, and `teacher_exp_11_plus` were generated from combining:
            * Beginning teachers and teachers with 1-5 years of experience into `teacher_exp_0to5`
            * Teachers with 11+ years of experience were combined into `teacher_exp_11_plus`
            * `teacher_exp_6to10` stayed the same. Teachers of 6-10 years of experience
    * There were an initial 1571 rows
        * The total number of rows after preperation and cleaning is 1391

* **Separate into train, validate, and test datasets**
 
* **Explore data to develop an understanding of what features affect a school's STAAR passing rate.**
   * Initial questions:
       * Do schools with more economically disadvantaged students have a lower average percent passing rate for STAAR exams?
       * Do schools with teachers that have more years of experience have a better average STAAR score passing rates?
       * Of schools with a large proportion of economically disadvantaged students, do the schools with higher average STAAR scores have higher expenses per student?
       * Do schools with above average economically disadvantaged students have significantly higher total expendature per student?
       * Is there a statisticaly significant correlation between the amount of extracurricular expendatures and algebra passing rates?
       * Is there a statisticaly significant correlation between student teacher ratio and all subjects passing rates?
       
* **Prep the data for modeling:**
    * Split data into X and y train
    * Scale all numeric data excluding target variables:
        * MinMaxScalar() was used to scale data
      
* **Develop a model to predict STAAR scores for `english_1`, `english_2`, `algebra`, `biology`, and `history`**
   * Regression models were used to predict STAAR scores
       * Linear Regression
       * Lasso Lars
       * Tweedie Regressor
       * Polynomial Regression
   * Evaluate models on train and validate data**
   * Select the best model based on the lowest RMSE and difference between in sample and out of sample data RMSE
   * Test the best model on test data
 
* **Draw conclusions**

## Data Dictionary:

* For a full glossary of all information provided by the TEA check this website:
    * https://tea.texas.gov/sites/default/files/comprehensive-tprs-glossary-2021.pdf


| **Feature** | **Definition** |
|:--------|:-----------|
|school_id| The id number of the school from TEA|
|english_1| English I, percent of students at approaches grade level or above for English I|
|english_2| English II, percent of students at approaches grade level or above for English II|
|algebra| Algebra, percent of students at approaches grade level or above for Algebra|
|biology| Biology, percent of students at approaches grade level or above for Biology|
|history| U.S. History, percent of students at approaches grade level or above for U.S. History|
|bilingual_or_english_learner| EB/EL Current and Monitored, percent of students in the dual-language program that enables emergent bilingual (EB) students/English learners (ELs) to become proficient in listening, speaking, reading, and writing in the English language through the development of literacy and academic skills in the primary language and English.|
|teacher_exp_0to5| Integer, number of teachers with 0-5 years of experience|
|teacher_exp_6to10| Integer, number of teachers with 6-10 numbers of experience|
|teacher_exp_11_plus| Integer, number of teachers with 11 or more years of experience|
|extracurricular_expend| The amount of funds (in dollars) spent on extracurriculuars per student|
|total_expend| The average total amount of funds (in dollars) spent per student|
|econdis| students that are from homes that are below the poverty line
|salary| Average Actual Salary, Average amount teachers are being paid in dollars|
|high_edu| Percent of teachers with a masters or doctorate degree|
|ratio| Count of the number of students per one teacher|



## Steps to Reproduce
1. Clone this repo
2. Use the function from acquire.py to scrape the data from the TEA website 
    * May take a few hours to web scrape.
3. Use the functions from prepare.py to prepare the data for exploration
4. Run the explore and modeling notebook
5. Run final report notebook


## Citation:
All data acquired from:
* https://rptsvr1.tea.texas.gov/perfreport/tprs/tprs_srch.html

Link to the final presentation slide deck:
* https://www.canva.com/design/DAFdeHe75pM/qSUa86WQ0Gtg3R7mET4Lyg/view?utm_content=DAFdeHe75pM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

Link to the Tableau dashboard:
* https://public.tableau.com/app/profile/andy.jensen8392/viz/CapstoneDashboard_16795800870340/Dashboard1?publish=yes
