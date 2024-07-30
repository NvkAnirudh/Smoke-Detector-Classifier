''' 
Any functionalities used across the application are initialized here
'''
import numpy as np 

# helper function to handle outliers using np.clip
def handle_outliers(df, col, q1, q3, iqr):
    lower_bound = q1[col] - 1.5*iqr[col]
    upper_bound = q1[col] + 1.5*iqr[col]

    # replacing values outside the bounds with the respective bounds
    df[col] = np.clip(df[col], lower_bound, upper_bound)