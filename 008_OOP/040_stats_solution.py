#%%
import numpy as np


#%%
heights = np.random.randint(low= 0, high=250, size = 50)


# %% Task: create a class that calculates count, sum, min, max, range, mean, and median of a given list
# Implement a method "overview" which shows all results at once
class Stats:
    def __init__(self, l) -> None:
        self.l = l

    def count(self):
        return len(self.l)
    
    def sum(self):
        return np.sum(self.l)
    
    def min(self):
        return np.min(self.l)
    
    def max(self):
        return np.max(self.l)
    
    def range(self):
        return np.ptp(self.l)
    
    def mean(self):
        return np.mean(self.l)
    
    def median(self):
        return np.median(self.l)
    
    def overview(self):
        print(f"Count: {self.count()}")
        print(f"Sum: {self.sum()}")
        print(f"Min: {self.min()}")
        print(f"Max: {self.max()}")
        print(f"Range: {self.range()}")
        print(f"Mean: {self.mean()}")
        print(f"Median: {self.median()}")
        
# Test 
data = Stats(heights)
data.overview()

# %%
