#%% Packages
import pandas as pd
import numpy as np
from plotnine import *

#%% Data Preparation
starwars = pd.read_csv('./data/Starwars.csv')
# %%
print(starwars.head())
# %%
def plot_height_mass(df):
    g = (ggplot(df)) + aes(x='height', y = 'mass') + geom_point() + geom_smooth(method='lm') + coord_cartesian(xlim=(0, 250))
    return g
# %%
plot_height_mass(starwars)
# %%
starwars[starwars['mass']>=1000]
# %%
starwars_filt = starwars[starwars['mass']< 1000]
# %%
starwars_filt.shape
# %%
plot_height_mass(starwars_filt)

#%% Modeling
from sklearn.linear_model import LinearRegression
# %%
X = np.array(starwars_filt['height']).reshape(-1, 1)
y = np.array(starwars_filt['mass']).reshape(-1, 1)
# %%
regressor = LinearRegression(fit_intercept=True)
regressor.fit(X, y)
# %%
print(f'Slope: ${regressor.coef_}')
print(f'Intercept: ${regressor.intercept_}')
# %% Create Prediction
y_pred = regressor.predict(X)
starwars_filt['y_pred'] = y_pred

# %%
ggplot(starwars_filt) + aes(x='height', y='mass', label='name') + geom_point() + geom_text() + geom_smooth(method='lm') + geom_point(aes(y='y_pred'), color= 'red')
# %%
from sklearn.metrics import r2_score

r2_score(y, y_pred)
# %%
