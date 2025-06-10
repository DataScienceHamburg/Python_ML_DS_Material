#%% Package
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# %%
df = pd.DataFrame(np.arange(3000).reshape((1000, 3)), columns=['x1', 'x2', 'y'])

# %%
df.head()
# %%
df.shape
# %% Train / Test split
X, y = df.loc[:, df.columns != 'y'], df['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# %%
print(f'X_train shape: {X_train.shape}')
print(f'y_train shape: {y_train.shape}')
# %% Train / Validation / Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# val: 0.2 = 0.8 * ratio
# ratio = 0.8/0.2 = 4

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size = 1/4)
print(f'X_train shape: {X_train.shape}')
print(f'y_train shape: {y_train.shape}')
print(f'X_val shape: {X_val.shape}')
print(f'y_val shape: {y_val.shape}')
# %%
