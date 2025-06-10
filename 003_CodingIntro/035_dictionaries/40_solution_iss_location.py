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
response['timestamp']
# %% Exercise 2:
# extract the longitude of ISS
response['iss_position']['longitude']
#%% Exercise 3: (Bonus)
# convert timestamp (Unix Epoch) to readable format
import datetime
datetime.datetime.fromtimestamp(1662480881)