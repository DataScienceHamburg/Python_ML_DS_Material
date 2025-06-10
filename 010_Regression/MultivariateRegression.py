# %% Multivariate Regression

# # Data Understanding
# %% [markdown]
# Wine variants of Portuguese "Vinho Verde" are analysed with regards to their chemical properties. Finally, we are interested how these chemical properties influence wine quality.
# 
# 
# These are our independent variables:
# 
# 1. fixed acidity 
# 2. volatile acidity
# 3. citric acid 
# 4. residual sugar 
# 5. chlorides 
# 6. free sulfur dioxide 
# 7. total sulfur dioxide 
# 8. density 
# 9. pH 
# 10. sulphates 
# 11. alcohol 
# 
# This is our dependent variable:
# 
# 12. quality (score between 0 and 10)
# %% [markdown]
# # Packages
import numpy as np
import pandas as pd
from plotnine import *
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import seaborn as sns

# %%
wine = pd.read_csv('./data/winequality-red.csv', sep=';')
# %%
wine.head()
# %%
wine.dtypes
# %%
wine.describe()
# %%
sns.pairplot(wine.iloc[:, 7:12], hue= 'quality')
# %%
wine.corr()
# %%
X_train = np.array(wine.loc[:, wine.columns != 'quality'])
y_train = np.array(wine['quality']).reshape(-1, 1)
# %%
regressor = LinearRegression()
regressor.fit(X_train, y_train)
# %%
regressor.coef_

#%%
wine['quality_pred'] = regressor.predict(X_train)
# %%
(ggplot(wine)) + aes(x='quality', y='quality_pred') + geom_point(alpha=0.1)
# %%
r2_score(y_true=wine['quality'], y_pred=wine['quality_pred'])
# %%
