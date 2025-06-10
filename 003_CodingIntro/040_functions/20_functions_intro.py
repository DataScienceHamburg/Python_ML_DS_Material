#%% most simple function
def hello_world():
    print('Hello World')

hello_world()
# %% typically with return statement
def hello_world2():
    return 'Hello World'

x = hello_world2()
x

# %% with arguments
def hello_world3(person):
    return f"Hello {person}"

hello_world3(12)


# %% with arguments and type hints
def hello_world4(person: str) -> str:
    return f"Hello {person}"

hello_world4('Lea')
# %%
