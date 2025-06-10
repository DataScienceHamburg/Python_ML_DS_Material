#%% TASKS:
# - check your current working directory
# - change it if necessary
# - create subfolder 'fibonaccy' if it does not exist
# - create a file {x.csv} for the first 10 Fibonacci numbers with x being the number
# Help: each Fibonacci number is the sum of its two predecessors, e.g. 1, 1, 2, 3, 5, 8, 13, ... 
# Result files: 1.csv, 2.csv, 3.csv, ...

#%%
import os 
import pandas as pd

# get first ten fibonacci numbers
def create_fibonacci_list():
    fib = [1,1]
    for i in range(10):
        fib.append(fib[-2]+fib[-1])
    return fib 

fib_numbers = create_fibonacci_list()
fib_numbers


#%% create files
def create_files():
    sub_folder = 'work_files'
    if not os.path.exists(sub_folder):
        os.makedirs(sub_folder)

    for f in fib_numbers:
        pd.DataFrame({}).to_csv(f"{sub_folder}/{f}.csv")

# %% list files
files_in_folder = os.listdir('./work_files')
files_in_folder
# %% extract parts of filename
# extract the numbers from each filename
[int(os.path.splitext(f)[0]) for f in files_in_folder]
# %%
