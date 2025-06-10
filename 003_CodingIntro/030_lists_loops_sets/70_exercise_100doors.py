#%%
#%% packages
import pandas as pd
import numpy as np

#%% init the dataframe
cnt_doors = 101
doors = [False] * cnt_doors
# %%
for i in range(1, cnt_doors):
            for j in range(i, cnt_doors, i):
                doors[j] = not doors[j]  # switch the door
# %% check open doors
for i in range(1, cnt_doors):
    if doors[i] == True:
        print(i)

