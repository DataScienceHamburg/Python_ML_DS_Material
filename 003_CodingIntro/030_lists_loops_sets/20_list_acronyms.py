# %% Learnings:
# create list from scratch
# append to list
# for loop over list

# %% create a list one-shot

acronyms = ['Bob', 'Alice', 'Eve']

# %% create a list from scratch and add values
acronyms = []
acronyms.append('Bob')
acronyms.append('Alice')
acronyms.append('Eve')

 
acronyms
# %%
acronyms.remove('Eve')
acronyms
# %% check if value exists in list
search_name = 'Alice'
if search_name in acronyms:
    print(f'{search_name} is in list')

# %% task: print each name in separate line
for acronym in acronyms:
    print(acronym)

