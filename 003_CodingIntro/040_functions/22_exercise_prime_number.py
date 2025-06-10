# %%
# prime if it has exactly two factors: 1 and the number itself (n)

#%% Function
def isPrime(value):
  for i in range(2,value):
    if (value % i) == 0:
      return False
  return True    
    
# %% Test
isPrime(15)
# %%