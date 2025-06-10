# %% 
import requests
# %%
api_endpoint = 'http://api.open-notify.org/iss-now.json'


# %% JSON
# JavaScript Object Notation
response = requests.get(api_endpoint).json()
print(response)

#%% Exercise 1:
# extract the timestamp

# %% Exercise 2:
# extract the longitude of ISS

#%% Exercise 3: (Bonus)
# convert timestamp (Unix Epoch) to readable format
