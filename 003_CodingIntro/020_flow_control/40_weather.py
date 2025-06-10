# Learnings:
# comparators in Python
# <, <=, ==, >=, >, !=

# %%
temperature = -30  # deg C

if temperature > 30:
    # all indented statements are code block 
    # usually: 4 spaces
    print('stay inside')
elif temperature < 0:
    print('stay inside')
else:
    print('go outside')

# %% combined conditional statement
if temperature < 0 or temperature > 30:
    print('stay inside')
else:
    print('go outside')


# %% not-keyword
temperature = 25
forecast = 'sunny'
if temperature > 10 and not forecast == 'rain':
    print('go outside')
else:
    print('stay inside')
# %% boolean variable
is_raining = True
if is_raining:
    print('stay inside')
