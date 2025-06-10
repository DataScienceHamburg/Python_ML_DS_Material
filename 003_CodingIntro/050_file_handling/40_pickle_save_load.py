#%% packages
import pickle

#%% data to be stored
my_list = [0, 5, -10]

#%% functions for storing / loading data
def save_obj(obj, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)

def load_obj(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

#%% Test it
save_obj(my_list, 'my_list.pkl')
# %%
load_obj('my_list.pkl')