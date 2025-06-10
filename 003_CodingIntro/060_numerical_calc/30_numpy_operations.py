#%% packages
import numpy as np

#%%
my_matrix = [1, 2],[3,4]
arr_2d = np.array(my_matrix)
arr_2d.reshape((1,4))
# %% 
# np.ones((3, 3))
# np.zeros((3, 3))
diagonal_ones = np.eye(3)

# %% change values based on value
diagonal_twos = diagonal_ones
# diagonal_twos[diagonal_twos == 1] = 2
diagonal_twos[diagonal_twos < 10] = 2
diagonal_twos
# %% change values based on position
diagonal_twos[1:] = 5  # change second to last row
diagonal_twos
# %% change columns
diagonal_twos[: , 2] = 10
diagonal_twos
# %% last row
diagonal_twos[-1: , :] = 100
diagonal_twos

# %% view vs. copy
# view
diagonal_ones = np.eye(3)
diagonal_view = diagonal_ones.view()  # affects both objects
diagonal_copy = diagonal_ones.copy()

diagonal_view[:, -1] = -50
print(f"diagonal_view: {diagonal_view}")
print(f"original: {diagonal_ones}")  # affected as well
print(f"diagonal_copy: {diagonal_copy}")


# %% operations
diagonal_ones[0].sum(axis=0)
# %%
diagonal_ones.prod()
# %%
diagonal_ones.mean()
# %%
diagonal_ones.min()
# %%
diagonal_ones.max()
# %%
diagonal_ones.argmax()
# %%
diagonal_ones.argmin()
# %% array flatten
my_arr = np.array([[1,2, 3],[4,5,6],[7,8,9]])
flat_arr = my_arr.reshape(my_arr.size)
# %%
my_arr.flatten()
# %% transpose
my_arr.T
# %% linspace
# number with equal distance
np.linspace(0, 20, 5)

# %% random
# create array of shape and provide values with uniform distribution from 0 to 1
np.random.rand(2)

#%% max, min, argmin and argmax
arr_random = np.random.rand(20)

# %%
# arr_random.min()  # get min value
# arr_random.max()  # get max value
arr_random.argmax() # get position of max value
arr_random.argmin() # get position of min value


# %%
arr = np.arange(20)
arr
# %%
arr + arr
# %%
arr * arr
# %% division by zero replaced by nan (no error)
arr / arr
# %% joining arrays (1D)
a1 = np.array([0, 1, 2])
a2 = np.array([3, 4, 5])
np.concatenate((a1, a2))
# %% joining arrays (2D)
a3 = np.array([[1, 2], [3, 4]])
a4 = np.array([[5, 6], [7, 8]])

np.concatenate((a3, a4), axis=1).shape
# %%
np.concatenate((a3, a4), axis=0).shape
# %% concatenates arrays along new axis
np.stack((a3, a4), axis=1).shape
# %% search with where
a5 = np.arange(20)
np.where(a5 > 10)

# %% sort descending
-np.sort(-a5)
# %%
