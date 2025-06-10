#%% packages
import pandas as pd
import numpy as np
import folium


# %%
df = pd.DataFrame({'city': ['Hamburg', 'Berlin', 'Munich'],
                  'lat': [53.5511, 52.5200, 48.1351],
                  'long': [9.9937, 13.4050, 11.5820]
})

# calculate median of given lat long coords
center = [np.median(df['lat']), np.median(df['long'])]
# %%
m = folium.Map(location=center, zoom_start=5)
m
# %% add all cities as markers to map
for i in range(len(df)):
    folium.CircleMarker(location=[df.loc[i, 'lat'], df.loc[i, 'long']], tooltip=df.loc[i, 'city'], color='blue').add_to(m)
m
# %%
