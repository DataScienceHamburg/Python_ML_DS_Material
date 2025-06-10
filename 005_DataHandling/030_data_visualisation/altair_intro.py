#%% packages
import seaborn as sns
import altair as alt 
import pandas as pd

#%%
titanic = sns.load_dataset("titanic")

alt.Chart(titanic).mark_bar().encode(
    alt.X('class'),
    y='count()'
)
# %%
filename = "Diamonds.csv"
diamonds = pd.read_csv(filename)
# %%
alt.Chart(diamonds[:100]).mark_point().encode(
    x='x',
    y='y',
    color='cut',
    size='price'
)
# %%
