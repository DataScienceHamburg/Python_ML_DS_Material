# Resampling Techniques

#%% Packages
import numpy as np
import pandas as pd
from plotnine import ggplot, aes, geom_point, geom_smooth
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split, KFold, LeaveOneOut, cross_val_score

#%% Data Import
wine = pd.read_csv('./data/winequality-red.csv', sep=';')

#%% Dependent and independent features and check shapes
X, y = np.array(wine.loc[:, wine.columns != 'quality']), np.array(wine.loc[:, wine.columns == 'quality'])
print(X.shape, y.shape)
#%% Train Test split with 20% testing / 80% training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#%% Train Linear Model and calculate R^2 score
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
r2_score(y_true=y_test, y_pred = y_pred)
# %% Cross Validation
kf = KFold(n_splits=10, shuffle=True)
kf.get_n_splits(X)
print(kf)


# %%
model = LinearRegression()
scores = []
for train_index, test_index in kf.split(X):
    X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
    model.fit(X_train, y_train)
    scores.append(model.score(X_test, y_test))
print(scores)
print(np.median(scores))
# %%
np.median(cross_val_score(model, X, y, cv=10, scoring = 'r2'))
# %% Leave One Out CV
np.median(cross_val_score(model, X, y, cv=1599, scoring = 'r2'))
# %%
from sklearn.model_selection import cross_val_predict
y_pred = cross_val_predict(model, X, y, cv=len(X))
# %%
y_pred.shape
# %%
r2_score(y, y_pred)
# %%
df = pd.DataFrame({'y_act': [i[0] for i in y.tolist()], 'y_pred': [i[0] for i in y_pred.tolist()]})
df
# %%
ggplot(df) + aes(x='y_act', y='y_pred') + geom_point(alpha=0.1) + geom_smooth(method = 'lm', color = 'red')
# %%
