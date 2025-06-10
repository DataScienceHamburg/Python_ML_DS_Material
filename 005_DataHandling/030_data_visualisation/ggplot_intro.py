# %% packages
import pandas as pd
from plotnine import *

# %%
filename = "Diamonds.csv"
diamonds = pd.read_csv(filename)

# %% EDA
diamonds.head()

# %% One Variable

# %% Discrete Feature
(ggplot(data=diamonds) 
  + aes(x = 'cut') 
  + geom_bar()
)

# %% Continuous Feature
(ggplot(diamonds) +
  aes(x = 'price') + 
  geom_density()
)

# %%
(ggplot(diamonds) +
  aes(x = 'price') + 
  geom_area(stat='bin')
)

# %% [markdown]
# # Two Variables

# %% Continuous X, Continous Y
(ggplot(data=diamonds[diamonds['cut'].isin(['Fair', 'Premium'])]) +
  aes(x='x', y='y', color='price', size ='carat') +
  geom_point() +
  facet_grid(['color','cut'])
  #scale_y_log10()
)

# %% Continuous X, Discrete Y
(ggplot(data=diamonds) +
  aes(x='price', y='clarity') + 
  geom_bin2d()
)

# %% Discrete X, Continuous Y
(ggplot(data=diamonds) +
  aes(x='clarity', y='price') + 
  geom_jitter(alpha=.2)
)

# %%
(ggplot(data=diamonds) +
  aes(x='clarity', y='price') + 
  geom_violin()
)

# %%
(ggplot(data=diamonds) +
  aes(x='clarity', y='price') + 
  geom_boxplot()
)

# %% Discrete X, Discrete Y
(ggplot(data=diamonds) +
  aes(x='clarity', y='cut') + 
  geom_jitter(alpha=.2)
)

# %%



