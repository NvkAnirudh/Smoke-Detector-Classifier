import sys
import os
import numpy as np
import pandas as pd 
from dataclasses import dataclass

from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    validation_data_path: str = os.path.join('artifacts','validation_data.csv')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def handling_outliers(self, X):
        try:
            # As can be seen in the boxplots in notebook, the features in the dataset contain outliers
            # Handling outliers
            q1 = X.quantile(0.25)
            q3 = X.quantile(0.75)
            iqr = q3 - q1

            features = X.columns

            # Handling the outliers for every column in the dataset (except the target variable)
            for feature in features:
                lower_bound = q1[feature] - 1.5*iqr[feature]
                upper_bound = q1[feature] + 1.5*iqr[feature]

                # replacing values outside the bounds with the respective bounds
                X[feature] = np.clip(X[feature], lower_bound, upper_bound)

            return X
        
        except Exception as e:
            raise CustomException(e, sys)
    
    def handling_multicollinearity(self, X):
        try:
            # As can be seen in the pairplot and heatmap from the juptyter notebook, there is linear relationship between few of the features (multicollinearity)
            # Handling multicollinearity with Variance Inflation Factor (VIF)
            vif = pd.DataFrame()
            vif['feature'] = X.columns
            vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]

            print('Features with their respective VIFs')
            print(vif.sort_values(by='VIF', ascending=False))

            # Threshold for VIF
            max_vif = 5

            # Intializing a flag to check if any of the variables are exceeding the VIF threshold
            flag = True

            while flag:
                vif = pd.DataFrame()
                vif['feature'] = X.columns
                vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]

                # Finding the variable with the highest VIF
                max_vif_feature = vif.loc[vif['VIF'].idxmax()]

                if max_vif_feature['VIF'] > max_vif:
                    # Removing the variable from X 
                    X = X.drop(max_vif_feature['feature'], axis=1)
                    print(f'Variable with high VIF (removed): {max_vif_feature["feature"]} {max_vif_feature["VIF"]}')
                else:
                    # If no variable exceeds the threshold, set the flag to False
                    flag = False

            print('Final variables after handling multicollinearity', X.columns)

            return X
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def feature_scaling(self, X):
        try:
            scaler = StandardScaler()

            # Fit and transform on X_train
            X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

            return X_scaled
        
        except Exception as e:
            raise CustomException(e, sys)

    
    def initiate_data_transformation(self):

        logging.info("Started Data Transformation Component")
        try:
            df = pd.read_csv('artifacts/raw_data.csv')

            # Initializing X and y for training purposes
            X = df.drop('Fire Alarm', axis=1)
            y = df['Fire Alarm']

            logging.info('Handling Outliers')

            X = self.handling_outliers(X)
            
            logging.info('Handling Multicollinearity')

            X = self.handling_multicollinearity(X)

            logging.info('Scaling the features')

            X_scaled = self.feature_scaling(X)

            # Tom's tasks: Split the data and store them in a csv file
        
        except Exception as e:
            raise CustomException(e, sys)