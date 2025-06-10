#%% package import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

#%% Data Source: California Housing
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing

#%% Data Import
X, y = fetch_openml(name="house_prices", as_frame=True, return_X_y=True)# %%

#%% 1. Combine X and y
# X covers all house information, y covers the price.
# Please combine both to one dataframe called housing, the values in y should then be called 'price'
# Hint: you don't need to use pd.merge
# Hint2: consider that X and y have different types
housing = X.copy()
housing['price'] = y

#%% 2. make yourself familiar with the columns of the dataframe



# %% 3. group the 'OverallQual' and get the min, max, mean price for the different conditions


# %% 4. find the unique values for represented 'Street' and create a dataframe for each street


# %% 5. check the number of rows for both dataframes


# %% 6. combine both dataframes to one new dataframe 'housing_combined' and check the number of rows


# %% 7. use the shown housing_types dataframe and convert it to a wide dataframe
# the columns shall represent the 'GarageType' and the indices the 'BldgType' 
housing_types = housing.groupby(['BldgType', 'GarageType']).agg({'price': np.mean}).reset_index()

# %%
