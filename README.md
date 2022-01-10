# Emotion Analysis

# 1. Dataset information:
We use and compare various different methods for sentiment analysis on tweets (using ML classfiers). The training dataset is expected to be a csv file of type tweet_id,sentiment,tweet where the tweet_id is a unique integer identifying the tweet, sentiment is about the tweet, and tweet is the tweet enclosed in "". 

# 2. Requirements
There are some general library and server requirements for the project and some which are specific to individual methods. The general requirements are as follows.

    1. numpy
    2. pandas
    3. pickle
    4. scikit-learn
    5. flask
    6. gunicorn
    
# 3. Usage

  1. Preprocessing:
      a. The CSV file is read through Pandas library and 'tweet_id' attribute is dropped. The dataframe is converted to a NumPy record array. 
         Append the labels in 'y' attribute and appending the subsentences or phrases in 'x' attribute with number of occurances. 
  
  2. The x and y datasets are split into training and test datasets using <mark>train_test_split</mark> function. 
