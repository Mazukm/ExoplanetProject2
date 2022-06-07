import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

class MachineLearning():


    def prep_data(df):
        """
        filters the data to the labels and features
        labels is the amount of planets 
        features is the information about the star
        one hot encodes teh rest of the data
        """
        labels = df["sy_pnum"]
        features =  df.loc[:,["st_teff","st_rad","st_metratio"
                              ,"st_spectype","st_logg"]]
        features = pd.get_dummies(features,  columns = ["st_metratio","st_spectype"])
        return labels, features

    def seperate_datasets(labels, features):
        """
        seperates the data set in the train and test sets
        """
        features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2)
        return features_train, features_test, labels_train, labels_test

    def train_model(labels_train, features_train):
        """
        trains a model using linear regression 
        """
        model = RandomForestRegressor().fit(features_train, np.array(labels_train))
        return model
    
    def test_model(labels_test, features_test, model):
        """
        runs the given model, and calculates the accuracy from taking the correct labels 
        and comparing to the output
        """
        test_predictions = model.predict(features_test)
        print('Test  Diviation:', mean_squared_error(np.array(labels_test).reshape(-1, 1), test_predictions))