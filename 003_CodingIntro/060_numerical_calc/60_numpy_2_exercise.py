#%% packages
import numpy as np


# %% A1. create an array with dim (10, 10) and values from 1 to 100 with two for loops
# hint: initialize the array with zeros to begin with
A1 = np.zeros((10, 10))

for i in np.arange(10):
    for j in np.arange(10):
        A1[i, j] = (i+1)*(j+1)

A1

# %% A2. create the same array with just one for loop
A2 = np.zeros((10, 10))
for i in np.arange(10):
    A2[i, :] = (i+1) * (np.arange(10) + 1)

A2


# %% A3. create the array with for loop
A3 = np.arange(1, 101).reshape(10, 10)
A3

# %%
