# %% Polynomial Regression

# This lecture shows how to create a higher-order polynomial regression.
# %% [markdown]
# What is polynomial regression? To understand this, we compare simple linear regression to it. In simple linear regression you fit an equation of the form:
# 
# $$y = \beta_0 + \beta_1 x$$
# 
# with
# 
# $\beta_0$ being the offset and
# 
# $\beta_1$ being the slope.
# %% [markdown]
# With polynomial regression this equation changes to:
# 
# $$y = \beta_0 + \beta_1 x + \beta_2 x^2 + ...$$
# %%
# %% [markdown]
# An additional term $\beta_2 x^2$ (or even higher terms) is created, which accounts for quadratic conditions.
# %% Packages
import numpy as np
import pandas as pd
from plotnine import *
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
import random
# %%
sample_data = pd.DataFrame(np.arange(-20, 40, 0.5), columns= ['x'])
sample_data['y'] = 50 + 0.25 * (sample_data['x']-5)**3
sample_data['y_noise'] = sample_data['y'] + np.random.normal(100, 500, sample_data.shape[0])
# %%
(ggplot(sample_data) 
 + aes(x='x', y='y_noise')
 + geom_point()
 + geom_line(aes(y='y'), color = 'red')
)
# %% Dependent / independent Features
X = np.array(sample_data['x']).reshape(-1, 1)
y = np.array(sample_data['y_noise']).reshape(-1, 1)
# %%
def model_and_visualisation(degree):
    poly_feat = PolynomialFeatures(degree=degree)
    x_poly = poly_feat.fit_transform(X)
    model = LinearRegression()
    model.fit(x_poly, y)

    # create preds
    sample_data['y_poly_pred'] = model.predict(x_poly)

    # visualise results
    g = (ggplot(sample_data)
     + aes(x= 'x', y = 'y_noise')
     + geom_point()
     + geom_line(aes(y = 'y'), color='red')
     + geom_line(aes(y = 'y_poly_pred'), color = 'green')
    )
    return g


# %%
model_and_visualisation(4)
# %% 
r2 = r2_score(sample_data['y_noise'], sample_data['y_poly_pred'])
r2

# %%
degree =5
p = degree
n = sample_data.shape[0]
adj_r2 = 1 - (1-r2)*(n-1)/(n-p-1)
adj_r2

# %%
