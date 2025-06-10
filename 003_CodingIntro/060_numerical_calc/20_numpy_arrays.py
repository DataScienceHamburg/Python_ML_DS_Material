#%% package
import numpy as np

#%% create array from list
my_list = [0, 1, 2, 3, 4]
arr = np.array(my_list)
arr
#%% create array
arr = np.arange(5)  # starts with 0
arr
# %%
arr = np.arange(2,5)  # specify start and end
arr

#%%
arr = np.arange(-2,15, 1.5)  # specify start and end
arr

# %% create array from list
np.array([2, 5, 8], dtype=np.float64)

# %% 2D
my_matrix = [1, 2],[3,4]
arr_2d = np.array(my_matrix)
arr_2d
# %% built-in functionality
#%% dimension of array
arr.shape  # shape of array

#%% reshape
arr_2d.shape
# %%
np.arange(4).reshape((2,2))
# %%
