# %% EXERCISE 1
def name_age(name, age):
    return f"{name} ist {age} Jahre alt."

#%% TEST 1
name_age('Kiki', 3)
# %%
#%% EXERCISE 2
def multiply(l):
    product = 1
    for i in l:
        product *= i
    return product

#%% TEST 2
my_list = [2, 4, 8]
multiply(my_list)

#%% EXERCISE 3
def currencyConversion(value, ratio = 1.1):
    return value * ratio
# %% TEST 3
currencyConversion(value = 20, ratio = 1.5)

# %%
currencyConversion(value = 20)
# %% EXERCISE 4
def simpleMath(a, b):
    sum = a + b
    diff = a - b
    mul = a * b
    div = a / b
    return sum, diff, mul, div

# %% TEST 4
simpleMath(12, 5)

#%% EXERCISE 5
def generateList(start, end):
    return list(range(start, end+1))
# %%
generateList(start = 10, end =20)
# %% EXERCISE 6
def findMaxVal(l):
    return max(l)


# %%
findMaxVal([2, 8, 10, -5, 11, 3])
# %% EXERCISE 7
def odd_or_even(val):
    return 'even' if val % 2 == 0 else 'odd'

# %% TEST 7
odd_or_even(7)
# %% EXERCISE 8
import math
def rotor_area(val):
    return math.pi * val**2
# %%
rotor_area(82)
# %%
import pandas as pd
df = pd.DataFrame({'Student': ['Stuart', 'Bob', 'Kevin'],
'Sport': [2, 3, 3], 'Art': [4, 2,1]})
# %%
