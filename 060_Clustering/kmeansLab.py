#%% Packages
# data handling
import numpy as np
import pandas as pd

# modeling
from sklearn.cluster import KMeans

# prepare sample data
from sklearn.datasets import make_blobs

# data visualisation
from plotnine import ggplot, aes, geom_point, labs
import seaborn as sns

#%% Data Preparation
X, y_true = make_blobs(n_samples=1000, 
                       centers=3,
                       cluster_std=0.7, 
                       random_state=123)



df = pd.DataFrame(X, columns=['x1', 'x2'])
df['y_true'] = [str(i) for i in y_true.tolist()]

# %%  Data Visualisation

# The graph shows the true labels of the clusters. The clusters are also clearly distinguishable.
(ggplot(df) + 
    aes(x='x1', y='x2') +
    geom_point() 
)

# %% Modeling
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# %%
centers = pd.DataFrame(kmeans.cluster_centers_)
centers.columns = ['x1', 'x2']
# %%
df['y_kmeans'] = kmeans.predict(X)
# %%
ggplot(data= df, mapping=aes(x='x1', y='x2')) + geom_point(mapping=aes(color='y_kmeans'))
# %%
sse = []
for k in range(1, 8):
    kmeans = KMeans(n_clusters=k) 
    kmeans.fit(X)
    sse.append(kmeans.inertia_)
# %%
sns.lineplot(x=range(1, len(sse)+1), y = sse)