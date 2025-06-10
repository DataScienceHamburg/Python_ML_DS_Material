#%% python
from zipfile import ZipFile

#%%
with ZipFile('my_archive.zip', mode='w') as archive:
    archive.write('working_dirs.py')

# %%
