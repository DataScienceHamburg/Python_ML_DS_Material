# %% [markdown]
# Import **pandas** as the required package for working with dataframes.

# %%
import pandas as pd

# A dataframe is a multi-dimensional table with rows and columns.

# %% Creating a Dataframe
# Usually you import a dataframe from a file, a SQL server, or a web-resource. But here I will show you how to create a dataframe from scratch.
# 
# You can create a dataframe based on lists, tuples, arrays. Here we develop it based on a dictionary.

# %%
data = {
    'A': [1,2,3],
    'B': [4,5,6],
    'C': [7,8,9]
}
df = pd.DataFrame(data=data)
df

# A dataframe has columns (here: A, B, C), and rows. The index is creating and starts with 0.

# # Import and Export of Dataframes

# You can export a dataframe into different formats like Excel, JSON, ... Here I export it to a CSV file.

# %%
filename = 'df.csv' 
df.to_csv(filename, index=False)

# Similarly the dataframe can be imported with **pandas**. There are many different read-functions to import from different formats.

# %%
df = pd.read_csv(filename)

# # Exploratory Data Analysis

# %% [markdown]
# You can explore the data with *head()* to see the first observations. If you are interested in the last observations go with *tail()*. The argument refers to the number of observations to be shown.

# %%
df.head(2)

# %% [markdown]
# Statistical properties are shown with the *describe()* method.

# %%
df.describe()

# %% [markdown]
# A general summary on the dataframe is provided by *info()* method.

# %%
df.info()

# %% [markdown]
# Often you are interested in getting the number of rows and columns. You can get this with the shape property.

# %%
df.shape

# %% [markdown]
# The column-names are stored in the property *columns*.

# %%
df.columns