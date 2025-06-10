#%% packages
import pandas as pd
import numpy as np

#%% Series
my_series = pd.Series(np.arange(3), index=['a', 'b', 'c'])
# %%
# my_series[0]  # access via index
my_series['a']  # access via label

#%% create dataframe
# from dict
my_dict = {'name': ['Bob', 'Stuart', 'Kevin'], 'grades': [1, 2, 3]}
df = pd.DataFrame(my_dict)
df
# %%
# from np array
# df = pd.DataFrame(np.random.rand(2, 2), columns=['height', 'width'])
# df.columns

# now set/change column names after creation
df = pd.DataFrame(np.random.rand(2, 2))
df.columns = ['height', 'width']
df
# %%


# %%
