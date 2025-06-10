#%% packages
import pandas as pd
import numpy as np

#%%
df = pd.DataFrame({'language': ['R', 'Python', 'SQL', 'R', 'R', 'Python', 'Python'], 
                    'year': [2020, 2020, 2020, 2021, 2022, 2022, 2022],
                    'users': [1E6, 2E6, 0.5E6, 1.1E6, 1.2E6, 2.2E6, 2.4E6]})
df
# %%
df['users'].plot()
# %%
import matplotlib.pyplot as plt
plt.plot(df.loc[df['language']=='Python', 'users'])
plt.plot(df.loc[df['language']=='R', 'users'])
plt.plot(df.loc[df['language']=='SQL', 'users'])
plt.show()
# %%
