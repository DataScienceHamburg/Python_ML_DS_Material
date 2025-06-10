#%% kwargs - keyword arguments
# parameters passed as dictionary
# 
#%%
def my_volume(**kwargs):
    print(kwargs)

my_volume(height=5, width=2, depth = 3)

# %% 
def convert_usd_to_aud(amount, rate=0.75):
    return amount / rate

# %%
#  3.	Create a new function convert_and_sum_list which will take a list of amounts, convert them to AUD, and return the sum: 

def convert_and_sum_list(usd_list, rate=0.75):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_aud(amount, rate=rate)
    return total

print(convert_and_sum_list([1, 3]))

# %% 
# Note that the function convert_and_sum_list didn’t need the rate argument.  It simply needed to pass it through to the convert_usd_to_aud function.  Imagine that instead of one argument, we had 10 that needed to be passed through.  There will be a lot of unnecessary code.  Instead, we will use the kwargs dictionary.

# 5.	Add the following function to conversion.py: 
def convert_and_sum_list_kwargs(usd_list, **kwargs):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_aud(amount, **kwargs)
    return total

print(convert_and_sum_list_kwargs([1, 3], rate=0.8))