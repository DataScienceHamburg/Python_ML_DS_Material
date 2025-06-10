#%% packages 
from timeit import timeit
import numpy as np
import time
#%%
#%%timeit
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [4, 5, 6, 7, 8, 9, 0, 1, 2]
z = []

for i, j in zip(x, y):
    
  z.append(i + j)
print(z)
# %%
#%%timeit
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [4, 5, 6, 7, 8, 9, 0, 1, 2]
z = np.add(x, y)
# %%
