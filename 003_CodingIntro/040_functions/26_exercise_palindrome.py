# %% Intro
# A palindrome is a word identical forwards and backwards
# examples: civic, deed, rotor
# special case: 'race car' is a palindrome if space is not regarded


# %% Function
import re
def isPalindrome(word):
    forward = ''.join(char for char in word.lower() if char.isalpha())
    print(forward)
    backward = forward[::-1]
    return forward == backward
# %% Test
isPalindrome('Race cars')
# %%
