#%% positional arguments args
# args is convention
# args is a tuple passing the function parameters


def my_sum(*args):
    print(args)

# %%
import numpy as np
def my_sum(*args):
    return np.sum(args)

#%% test it
my_sum(1,5)

# %% kwargs
def pass_kwargs(**kwargs):
    print(f"kwargs:, {kwargs}")
    for kw in kwargs:
        print(kw, '-', kwargs[kw])

pass_kwargs(a=5, b=15, c=25)

# %% kwargs
def colors(green, red, **kwargs):
    print(f'green: {green}')
    print(f'red: {red}')

kw = {'green': 1, 'red': 2}
colors(**kw)


# %%
