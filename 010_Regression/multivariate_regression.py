#%% packages
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures

#%% prepare polynomial features
poly = PolynomialFeatures(degree=1, include_bias=False)

#%%
df = pd.read_csv("data/updated_pakwheels.csv")
df.columns

#%% check number of different names in 'Name' column
df['Assembly'].nunique()

#%% select independent features
selected_features = ["Price", "Model Year", "Mileage", 'Engine Type', 'Engine Capacity', 'Transmission', 'Color', 'Body Type', 'Assembly']
df_sel = df[selected_features]
df_sel

#%% treatment for categorical data
df_sel_dummies = pd.get_dummies(df_sel, columns=['Engine Type', 'Transmission', 'Body Type', 'Color', 'Assembly'], dtype=float)
df_sel_dummies

#%% separate independent / dependent features 
X = df_sel_dummies.drop(columns='Price')
y = df_sel_dummies[['Price']]


# %% create train / test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#%% normalize data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

#%% scale test data
X_test_scaled = scaler.transform(X_test)

#%% polynomial features
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

#%% model training
model = LinearRegression()
model.fit(X_train_poly, y_train)

#%%
len(model.coef_[0])

#%% model inference
y_test_pred = model.predict(X_test_poly)

# %% scatter plot with x-range 0-2e7, y-range 0-2e7
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
sns.scatterplot(x=np.array(y_test).flatten(), y=np.array(y_test_pred).flatten(), ax=ax)
# ax.set_xlim(0, 2e7)
# ax.set_ylim(0, 2e7)
plt.show()
# %% extract r^2
r2_score(y_test,y_test_pred)

# %% distribution of residuals
residuals = y_test - y_test_pred
sns.histplot(residuals, bins=100)
plt.show()

# %%


