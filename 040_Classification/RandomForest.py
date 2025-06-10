# %% Packages
# Data Handling
from os import pipe
import numpy as np
import pandas as pd

# Modeling
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Visualisation
import seaborn as sns

#%% Data Import
diabetes = pd.read_csv('data/diabetes.csv')
# %% Data Understanding
corr = diabetes.corr()

# generate mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

sns.heatmap(corr, mask=mask, cmap=cmap, vmin=-1, vmax=1, center=0,
            linewidths=.5, cbar_kws={"shrink": .5})


# %% Separate Independent / Dependent Features
X = diabetes.drop(['Outcome'], axis=1)
y = diabetes['Outcome']


# %% Train / Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

#%% Modeling

# Baseline Classifier
total = len(y_test)
sum_y_test = np.sum(y_test)
max_group = [sum_y_test if sum_y_test > (total-sum_y_test) else (total-sum_y_test)]
max_group[0] / total * 100

# %% Random Forest Classifier
steps = [
    ('scaler', StandardScaler()),
    ('random_forest', RandomForestClassifier(n_estimators=1000, random_state=42, bootstrap=True))
]
pipeline = Pipeline(steps)

clf = pipeline.fit(X_train, y_train)

# %%
y_pred = clf.predict(X_test)
confusion_matrix(y_test, y_pred)

# %%
accuracy_score(y_test, y_pred)

#%% Importances
importances = list(RandomForestClassifier(n_estimators=1000, random_state=42, bootstrap=True).fit(X_train, y_train).feature_importances_)
# %%
feature_names = X_train.columns
# %%
feature_importance = pd.DataFrame([(feature_names, round(importances, 2)) for feature_names, importances in zip(feature_names, importances)], columns=['feature', 'importance'])
# %%
g = sns.barplot(data=feature_importance, x='feature', y='importance')
g.set_xticklabels(labels=feature_importance['feature'], rotation=90)
# %%
