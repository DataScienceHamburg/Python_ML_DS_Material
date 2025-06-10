#%% packages
import seaborn as sns
import pandas as pd

# %%
filename = "Diamonds.csv"
diamonds = pd.read_csv(filename)
diamonds['volume'] = diamonds['x'] * diamonds['y'] * diamonds['z']
#%%
sns.set_theme(style='darkgrid')
s= sns.relplot(data=diamonds.iloc[1500:2000, :], x='carat', y = 'price', size='depth', hue='cut', style='clarity')
s.set(ylim = (3000, 3150))
# %%
