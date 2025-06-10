#%% packages
import numpy as np
# %% E1:
# - create a matrix with dimension 10x10
# - fill it with values from 0 to 99
# - replace all values which are not square-numbers, with 0

arr = np.arange(100).reshape((10, 10))
arr


#%%
def is_number_square(val):
    sqrt_val = np.sqrt(val)
    if (sqrt_val - int(sqrt_val) == 0):
        return val
    else:
        return 0

# %%
row_id = 0
for x in np.arange(10):
    for y in np.arange(10):
        arr[x, y] = is_number_square(arr[x, y])
        
arr 