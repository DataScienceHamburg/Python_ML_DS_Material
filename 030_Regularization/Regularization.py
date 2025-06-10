# Regularization

#%% Packages
import numpy as np 
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso

from plotnine import ggplot, aes, geom_point


# %% Data Import
boston = load_boston()
df_boston = pd.DataFrame(boston.data, columns=boston.feature_names)
df_boston['y'] = boston.target
df_boston
# %%  Dependent / independent features
X = df_boston.drop('y', axis=1)
y = df_boston['y']



# %% Train / Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
print(X_test.shape, y_test.shape)

# %%
lr = LinearRegression()
lr.fit(X_train, y_train)

ridge_small_alpha = Ridge(alpha = 0.01)
ridge_small_alpha.fit(X_train, y_train)

ridge_large_alpha = Ridge(alpha = 1000)
ridge_large_alpha.fit(X_train, y_train)

lasso = Lasso()
lasso.fit(X_train, y_train)
# %% Test scores
lr_test_score = lr.score(X_test, y_test)
rigde_small_alpha_score = ridge_small_alpha.score(X_test, y_test)
ridge_large_alpha_score = ridge_large_alpha.score(X_test, y_test)
lasso_test_score = lasso.score(X_test, y_test)

print(f'Linear Reg: {lr_test_score}')
print(f'Ridge (small alpha): {rigde_small_alpha_score}')
print(f'Ridge (large alpha): {ridge_large_alpha_score}')
print(f'Lasso: {lasso_test_score}')

# %% 
coefs = pd.DataFrame({'lr': lr.coef_, 'ridge_small': ridge_small_alpha.coef_, 'ridge_large': ridge_large_alpha.coef_, 'lasso': lasso.coef_})
coefs['coef'] = coefs.index
coefs_long = coefs.melt(id_vars='coef')
coefs_long
# %%
(ggplot(coefs_long) + aes(x='coef', y='value', color='variable') + geom_point(alpha = .5))
# %%
