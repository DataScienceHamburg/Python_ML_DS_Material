#%% learnings:
# - if, else
# - f-string

# %% package import
import random

# %%
roll = random.randint(1, 6)
# %%
guess = int(input('guess dice roll:'))

if guess == roll:
    print('match')
else:
    print(f'Wrong. You guessed {guess}, dice rolled {roll}')

# %%