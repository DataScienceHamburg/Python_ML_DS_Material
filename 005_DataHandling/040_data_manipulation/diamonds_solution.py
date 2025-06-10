#%%
import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_bar, labs, ggsave
#%% 0. add required packages at the top of this script

# %% 1. import dataset from subfolder "data"
df = pd.read_csv('data/diamonds.csv', index_col=None)
# %% 2. how many rows and columns does it have
df.shape

# %% 3. which columns does it have?
df.columns

# %% 4. There is a column named 'Unnamed: 0'. Please delete it.
df.drop(columns='Unnamed: 0', inplace=True)

# %% 5. which levels does column cut have?
df['cut'].unique()

# %% 6. create a barplot for diamonds and their cut's
g = ggplot(data = df) + aes('cut') + geom_bar() + labs(x = 'Cut', y = 'Count [-]', title="Diamonds Cut's Count")
g
#%% 7. save the graph as png-file
ggsave(g, 'diamonds_cut.png')

# %% 8. find out what the median price per cut is.
df.groupby('cut')['price'].agg(np.mean)

# %% 9. Create two filtered dataframes which only have the cut 'Ideal' and 'Premium'. Store it in the dataframes 'df_cut_ideal' and 'df_cut_premium'
df_cut_ideal = df[df['cut'] == 'Ideal']
df_cut_premium = df[df['cut'] == 'Premium']

# %% 10. stack the dataframes together to get a combined version df_cut_ideal_premium
df_cut_ideal_premium = pd.concat([df_cut_ideal, df_cut_premium])

# %% 11. save the dataframe to a csv file in subfolder data: 'df_cut_ideal_premium.csv'
df_cut_ideal_premium.to_csv('data/df_cut_ideal_premium.csv')

# %%
