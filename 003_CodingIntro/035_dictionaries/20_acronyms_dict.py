# %% 
# can hold everything
# key: value

# %%creation on one shot
acronyms = {
    'LIFE': 'Learning is fun and exciting',
    'MATH': 'Mental abuse to humans',
    'LIVE': 'Learning Important Values Everyday'
}

# %% sequential creation
acronyms = {}
acronyms['LIFE'] = 'Learning is fun and exciting'
print(acronyms)
del acronyms['LIFE']
acronyms
# %% accessing non-existing key -> key error
acronyms['NON']


# %% avoid key error with get
definition = acronyms.get('NON')  # returns None instead of error
# None...absence of value, evaluates to False in conditional

# %%
if definition:
    print(definition)
else:
    print('no such key')
# %%
for key, value in acronyms.items():
    print(f'{key} has value: {value}')
# %%
