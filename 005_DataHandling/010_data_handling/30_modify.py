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

# # Adding/Modifying Columns

# %%
df['D'] = list(range(10,13))
df

# %% [markdown]
# # Delete Rows or Columns

# %% [markdown]
# If you want to delete a column use method *drop()* and specify the column name. The argument axis needs to be 1 for columns. With inplace set to true the dataframe is directly modified.

# %%
df.drop('C', axis=1, inplace=True)
df

# %% [markdown]
# Similarly you can delete rows by specifying the index of the row, the axis is 0 for rows and inplace is set to true to change the dataframe directly.

# %%
df.drop(1, axis=0, inplace=True)
df

# %% [markdown]
# # Apply a lambda function to a column

# %% [markdown]
# You can also apply a specific function to a column.

# %%
my_func = lambda x: x + 2

df['E'] = df['A'].apply(my_func)
df

# %% [markdown]
# # Reshape your dataframe structure

# %% [markdown]
# You can reshape your dataframe structure from wide data to tidy data and vice versa. We are starting with wide-data.

