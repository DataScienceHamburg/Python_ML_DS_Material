#%% packages
import pandas as pd
import numpy as np

#%%
df = pd.DataFrame({'language': ['R', 'Python', 'SQL', 'R', 'R', 'Python', 'Python'], 
                    'year': [2020, 2020, 2020, 2021, 2022, 2022, 2022],
                    'users': [1E6, 2E6, 0.5E6, 1.1E6, 1.2E6, 2.2E6, 2.4E6]})
df

# %% understand grouping
for name, group in df.groupby('language'):
    mean_val = group['users'].mean()
    print(f"{name}: {mean_val}")

# %% group on a column and average over all other cols
# df.groupby('language').mean()
df.groupby('language').agg(np.mean)
# %% group on a column, average over a specific column
df.groupby('language')['users'].mean()
# %% group by multiple columns
df.groupby(['language', 'year'])['users'].mean()
# %% several aggregation functions
df.groupby('language').agg({'users': ['mean', 'min', 'max', 'sum']})

# %%
df.groupby('language').agg([np.mean, np.sum])

# %%
import pandas as pd
data = {'group_col': ['A', 'B', 'C', 'A', 'B', 'A'],
                   'value_col': [0, -2, 5, 2, 2, 4]}
df = pd.DataFrame(data)
df


#%%

# %%
for name, group in df.groupby('group_col'):
    group_values = group['value_col'].tolist()
    print(f"{name}: {group_values}")
# %%
df.groupby('group_col').agg({'value_col': [np.mean, np.sum]})

# %%
df.groupby('group_col').size()
# %%
