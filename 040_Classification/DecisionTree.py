# %% Decision Tree
# %% [markdown]
# A decision tree is a flowchart-like tree structure where an internal node represents feature(or attribute), the branch represents a decision rule, and each leaf node represents the outcome. 
# 
# [source](https://www.datacamp.com/community/tutorials/decision-tree-classification-python)
# %% Required Packages
# Data Handling
import numpy as np
import pandas as pd

# Modeling
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Visualisation
import seaborn as sns

# %% Data Prep
diabetes = pd.read_csv('./data/diabetes.csv')

# %%
diabetes.head()
# %%
diabetes.describe()
# %%
corr = diabetes.corr()
sns.heatmap(corr)
# %% Independent / dependent features
X = diabetes.drop(['Outcome'], axis = 1)
y = diabetes['Outcome']

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# %%
steps = [
    ('scaler', StandardScaler()),
    ('decision_tree', DecisionTreeClassifier())
]

pipeline = Pipeline(steps)

clf = pipeline.fit(X_train, y_train)

y_pred = clf.predict(X_test)
# %% Baseline Classifier Performance
(1-np.sum(diabetes['Outcome']) / diabetes.shape[0]) *100

# %% Our Classifier
confusion_matrix(y_test, y_pred)
# %%
accuracy_score(y_test, y_pred)
# %%
from sklearn import tree
dec_tree = DecisionTreeClassifier()
dec_tree.fit(X_train, y_train)
tree.plot_tree(dec_tree)
# %%
