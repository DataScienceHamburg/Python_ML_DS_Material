# %% E1: sum all expenses from list of expenses
# sample: expenses = [1, 5.5, 8, 25, 3]
# expected result: total: 42.5

expenses = [1, 5.5, 8, 25, 3]
total = 0
for i in expenses:
    total += i

print(f'total: {total}')

# %% show all expenses in separate line
for i in range(len(expenses)):
    print(expenses[i])

# %%
