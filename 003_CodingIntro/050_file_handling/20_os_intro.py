#%%
import os

#%% get cwd
os.getcwd()
# %% get folder content
os.listdir('.')
# %% create subfolder
subfolder_name = 'my_subfolder'
subfolder_exists = os.path.exists(subfolder_name)
if not subfolder_exists:
    os.makedirs(subfolder_name)
# %%
