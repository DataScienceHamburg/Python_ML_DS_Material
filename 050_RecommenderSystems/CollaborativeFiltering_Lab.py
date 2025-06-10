#%% Packages
from surprise import SVD, KNNWithMeans
from surprise.model_selection import train_test_split
from surprise import accuracy
from surprise import Dataset
from surprise import Reader
import os
import pandas as pd


# %% Data Prep
file_path = 'data/collabFiltering/ml-100k/u.data'
reader = Reader(line_format='user item rating timestamp', sep='\t')
data = Dataset.load_from_file(file_path, reader)
# %% Train / Test
trainset, testset = train_test_split(data, test_size=0.25)


# %% Model Training
svd = SVD()
svd.fit(trainset)

#%% Model Evaluation
preds = svd.test(testset)
accuracy.rmse(preds)

# %%
uid = str(196)
iid = str(302)
svd.predict(uid, iid, verbose=True)

# %%
item = pd.read_csv('data/collabFiltering/ml-100k/u.item', sep='|', encoding='latin-1', header=None, usecols=[0, 1], names=['id', 'name'])
# %%
item[item.id==302]
# %%
