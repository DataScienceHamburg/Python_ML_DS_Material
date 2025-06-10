#%% packages
import pandas as pd

# %%
data = {
    'student': ['Stuart', 'Bob', 'Kevin'],
    'math': [2,3,3],
    'sport': [3,1,2],
    'art': [4,2,1]
    
}
df_wide = pd.DataFrame(data=data)
df_wide

# %% test
df_long = df_wide.melt(id_vars= ['student'], 
             var_name = 'subject',
             value_name = 'grade')
df_long

#%% value_vars can be used as filter
# here: subject 'art' is not converted
df_long = df_wide.melt(id_vars= ['student'], 
             var_name = 'subject',
             value_name = 'grade', value_vars=['math', 'sport'])
df_long

# %%
df_wide2 = df_long.pivot(index='student', columns='subject', values='grade', )
df_wide2


# %% index names
# df_wide does not have an index name, df_wide2 got one created
# df_wide.index
df_wide2.index

# similar for column, df_wide2 got a name

#%% create graph
# barplot uses wide format
df_wide2.plot.bar()

#%%
df_wide_wo_index = df_long.pivot(index='student', columns='subject', values='grade', ).reset_index().rename_axis(None, axis=1)
df_wide_wo_index

#%%
df_wide2.index

# %%
