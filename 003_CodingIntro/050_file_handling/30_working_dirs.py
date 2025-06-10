#%% packages
import os

#%% current working directory
os.getcwd() # get current working dir
# os.chdir() # change current working dir
# %% create a subfolder if it does not exist
subfolder_name = 'work_files'
subfolder_exists = os.path.exists(subfolder_name)
if not subfolder_exists:
    os.makedirs(subfolder_name)
# %%
