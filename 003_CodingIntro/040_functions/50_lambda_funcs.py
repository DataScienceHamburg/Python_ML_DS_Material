#%% lambda function 
# can be used as anonymous function
# less overhead, e.g. no name
# keyword lambda
# bound variable
# body


#%% one argument
multiply_by_ten = (lambda x: x * 10)
multiply_by_ten(5)

# %% multiple arguments
x = lambda a, b : a / b
x(15, 3)


# %% can be used as anonymous function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mydoubler(10)

# %% can be combined with filter
# example: keep only numbers divisible by 5 without residual
l = [1, 2, 5, 10]
list(filter(lambda x: (x % 5 == 0), l))

# %%
