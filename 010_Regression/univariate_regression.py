
#%% packages
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression

#%% load data
df = pd.read_csv('data/house_prices_dataset.csv')
df

# add some noise to the data
df['price_noised'] = df['price'] + np.random.randn(len(df)) * 10000

#%% visualize data
sns.scatterplot(x='area', y='price_noised', data=df)

#%% model
model = LinearRegression()
model.fit(df[['area']], df['price_noised'])

# %% extract coefficients
print(f"bias: {model.intercept_}")
print(f"slope: {model.coef_}")

# %% create predictions
# df['price_pred'] = model.intercept_ + model.coef_ * df['area']
df['price_pred'] = model.predict(df[['area']])

#%% visualise scatter plot + predicted points as line
sns.scatterplot(x='area', y='price_noised', data=df)
sns.lineplot(x='area', y='price_pred', data=df, color='red')




# %%
