#%% package imports
import random

#%%
roll = random.randint(1, 6)

guess = int(input('guess dice roll:'))
guess

if guess == roll:
    print("Congrats. You guessed right.")
else:
    print(f"Wrong. You guessed {guess}, dice rolled {roll}")
# %%
