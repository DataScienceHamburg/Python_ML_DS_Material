#%% packages
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
# import SVR
from sklearn.svm import SVR
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt

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




#%% model training
steps = [
    ("scaler", StandardScaler()),
    ("poly", PolynomialFeatures(degree=1, include_bias=False)),
    # ("model", LinearRegression())
    ("model", SVR(kernel='linear'))
    # Ridge Regression
    # ("model", Ridge(alpha=0.1))
    # ("model", Lasso(alpha=0.1))
]

pipeline = Pipeline(steps)
pipeline.fit(X_train, y_train)

#%% extract coefficients
pipeline.named_steps['model'].coef_

#%% direct scoring of pipeline
# pipeline.score(X_train, y_train)
pipeline.score(X_test, y_test)


#%% model inference
y_test_pred = pipeline.predict(X_test)

# %% scatter plot with x-range 0-2e7, y-range 0-2e7
fig, ax = plt.subplots()
sns.scatterplot(x=np.array(y_test).flatten(), y=np.array(y_test_pred).flatten(), ax=ax)
ax.set_xlim(0, 2e7)
ax.set_ylim(0, 2e7)
plt.show()
# %% extract r^2
r2_score(y_test,y_test_pred)

# %% distribution of residuals


