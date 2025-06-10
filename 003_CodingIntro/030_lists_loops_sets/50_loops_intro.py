# %%
for char in 'Hamburg':
    print(char)
# %%
for i in range(1, 10):
    print(i)
# %%
for i in range(10):
    print(i)

# %% changed range start, end, step
for i in range(1, 11, 2):
    print(i)

# %% negative range
for i in range(3, 0, -1):
   print(i)
# %% iterate over list
names = ['Albert', 'Leonardo', 'Alan']
for name in names:
    print(name)

# %% Countdown
for i in range(10, -1, -1):
    print(i)
    if i==0:
        print('TakeOff')
# %% loop with else
for i in range(10, 0, -1):
    print(i)
else:  # executed when loop finishs normally
    print('TakeOff')

# %% for loop with if / else
for i in range(2, 8):
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')
# %% exit the loop early with "break"
values = [0, 12, 23, 42, 54, 99]
for i in values:
    if i == 42:
        break
    else:
        print(i)
else:
    print('loop finished normally')

# %% skip the current iteration and jump to next one
for char in "Hamburg":
    if char == 'b':
        continue
    else:
        print(char)

# %%
