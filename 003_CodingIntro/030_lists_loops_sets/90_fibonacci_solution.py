#%% Fibonacci Sequence
# --------------------
# Do you want to find out how many rabbits there are after x generations? Fibonacci found the mathematical number series that describes it. This series can be used for modeling other growth processes as well, e.g. plants. Besides this we learn its connection to Golden Ratio, and a lot about vectors handling.

# At first you should know how this series looks like and how it is calculated. The first six elements are
# 1, 1, 2, 3, 5, 8, …


#%% Task: Create a function which returns the n-first Fibonacci numbers!

def fibonacci(element_nr = 10):
    fib = [1, 1]
    for i in range(3, element_nr+1):
        next_element = fib[-1] + fib[-2]
        fib.append(next_element)
    return fib

fibonacci(4)
# %%
