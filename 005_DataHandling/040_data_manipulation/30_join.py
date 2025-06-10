#%% packages
import pandas as pd
import numpy as np

#%% prepare dataframes
# use main characters of animated films

minions = pd.DataFrame({
    'student': ['Stuart', 'Bob', 'Kevin', 'Gru'],
    'art': [4,2,1, 2]
    
})
print(f"minions:\n {minions}")

despicable_me = pd.DataFrame({
    'student': ['Agnes', 'Margo', 'Edith', 'Gru'],
    'sport': [1,2,2, 3]
    
})
print(f"despicable me:\n {despicable_me}")






frozen = pd.DataFrame({
    'student': ['Anna', 'Elsa', 'Olaf'],
    'art': [4,2,1]
})
print(f"frozen:\n {frozen}")

simpsons = pd.DataFrame({
    'student': ['Bart', 'Lisa'],
    'math': [5,1],
    'sport': [1,5]
    
})
print(f"simpsons:\n {simpsons}")

#%% left join
# how: left, right, inner, outer
# minions.merge(right=despicable_me, how='right', on='student', indicator=True)
minions.merge(right=despicable_me, how='right', left_on='student', right_on='student', indicator=True)

#%% join via index
despicable_me_index = despicable_me.copy()
despicable_me_index.index = despicable_me_index['student']
despicable_me_index.drop(columns=['student'], axis=1, inplace=True)
print(f"despicable me index:\n {despicable_me_index}")

minions.merge(right=despicable_me_index, how='right', left_on='student', right_index=True, indicator=True).reset_index(drop=True)



# %% append rows
minions.append(frozen)
# %% alternatively
pd.concat([minions, frozen])
# %% append columns
pd.concat([minions, simpsons])

# %%
