# %% [markdown]
# # Import Packages

# %%
import numpy as np
import pandas as pd
from plotnine import *
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import seaborn as sns

# %% [markdown]
# # Import Data

# %%
airfoil = pd.read_csv('./data/airfoil_noise.txt', sep='\t', names=['frequency', 'aoa', 
                                                                   'chord_length','free_stream_vel', 
                                                                   'ss_displacement_thickness', 'spl'])

# %% [markdown]
# # Exploratory Data Analysis (EDA)

# %%
airfoil.head()

# %%
airfoil.describe()

# %%
sns.pairplot(airfoil)

# %% [markdown]
# # Model Creation

# %%
X_train = np.array(airfoil.loc[:, airfoil.columns != 'spl'])
y_train = np.array(airfoil['spl']).reshape(-1, 1)

# %%
regressor = LinearRegression()
regressor.fit(X_train, y_train) 

# %% [markdown]
# # Create Predictions

# %%
airfoil['spl_pred'] = regressor.predict(X_train)

# %% [markdown]
# # Correlation Plot

# %%
(ggplot(airfoil) 
 + aes(x='spl', y='spl_pred') 
 + geom_point(alpha=0.1)
 + labs(x='Actual SPL [dB]', y='Predicted SPL [dB]', title='Correlation Plot')
 + geom_smooth(method='lm', se=False)
)

# %% [markdown]
# # Calculate Metrics

# %%
r2_score(y_true=airfoil['spl'], y_pred=airfoil['spl_pred'])


