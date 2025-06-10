#%% packages
import random
#%%
def clickBaitGenereator():
    PERSONS = ['Germans', 'Bavarians', 'Italians']
    NOUNS = ['Cats', 'Dogs', 'Diets', 'Robots']
    return f"What {random.choice(PERSONS)} don\'t want you to know about {random.choice(NOUNS)}!"

#%% test
clickBaitGenereator()
# %%
