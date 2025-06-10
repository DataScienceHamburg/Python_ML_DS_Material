#%%
temperature = 15

# too hot
if temperature >= 30:
    print('stay inside. It is too hot outside')
# too cold
elif temperature < 0:
    print('stay inside. It is too cold outside')
# every normal condition
else:
    print('go outside. Enjoy the weather')


# %% combined conditional statement
if temperature >= 30 or temperature < 0:
    print('stay inside')
else:
    print('go outside')

# %% not-keyword
temperature = 25
forecast = 'sunny'

temperature_lower_threshold = 0
if temperature > temperature_lower_threshold and not forecast == 'rain':
    print('go outside')
else:
    print('stay inside')
    
#%%
is_raining = True
if is_raining:
    print('stay inside')
    

# %%
