#%% packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#%% 1D data -> automatic x labels
plt.plot([0, 2, 5, 6])
plt.title('my first plot')
plt.xlabel('automatically generated')
plt.show()


#%% 2D data
plt.plot([1, 3, 5, 7], [-10, 5, 25, 20])

#%% formatting
# color and line type: default b-, 
plt.plot([1, 3, 5, 7], [-10, 5, 25, 20], 'go')
plt.axis([0, 10, -15, 30])  # [xmin, xmax, ymin, ymax]

#%% multiple series
my_range = np.arange(0, 10, 1)
# plt.plot(my_range, my_range)
# plt.plot(my_range, my_range, 'b-')
plt.plot(my_range, my_range, 'b-o', my_range, my_range**0.5, 'g-s', my_range, my_range**1.5, 'r-^')


#%% Data Import
filename = "Diamonds.csv"
diamonds = pd.read_csv(filename)

# %% additional dimensions
diamonds['volume'] = diamonds['x'] * diamonds['y'] * diamonds['z']
plt.scatter(data=diamonds.iloc[:100, :], x='carat', y = 'depth', s='price', c='volume')
plt.xlabel('carat')
plt.ylabel('depth')
plt.colorbar(label='volume')
plt.show()

# %%
