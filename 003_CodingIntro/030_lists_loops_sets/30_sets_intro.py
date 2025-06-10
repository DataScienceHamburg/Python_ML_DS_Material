# %% set creation
s1 = set([1,2,3,4,5,6])
print(s1)

s2 = set([1,2,2,3,4,4,5,6,6])
print(s2)

s3 = set([3,4,5,6,6,6,1,1,2])
print(s3)

# %% 
s4 = {"apple", "orange", "banana"}
print(s4)

s4.add('pineapple')
print(s4)
# %% set operations
s5 = {1,2,3,4}
s6 = {3,4,5,6}

# union
print(s5 | s6)
print(s5.union(s6))

# %% intersection
print(s5 & s6)
print(s5.intersection(s6))

# %% difference
print(s5 - s6)
print(s5.difference(s6))

# %% issubset
print(s5 <= s6)
print(s5.issubset(s6))

s7 = {1,2,3}
s8 = {1,2,3,4,5}

print(s7 <= s8)
print(s7.issubset(s8))

# %%
my_set = {'Bob', 'Alice', 'Eve', 'Bob'}
my_set
# %%

