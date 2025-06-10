#%% Logistic Regression

# The dataset is provided by UCI Machine Learning repository and deals with direct marketing of a bank. The target variable describes a customer subscribing (1) to a deposit or not (0).


# %% Packages
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from imblearn.over_sampling import SMOTE

from plotnine import ggplot, aes, geom_bar, labs

#%% Data Preparation

banking = pd.read_csv("./data/direct_marketing.csv")

#%% 
banking.describe()

#%% 
banking.head()

#%%  Target Variable
(ggplot(data=banking) +
 aes(x='y') +
 geom_bar() +
 labs(title = "Target Variable Count", y = "Count", x = "Target Variable")
)
# %% Filter Data

# The new object banking_filt only holds these information:

# 'age','duration','campaign', 'pdays', 'previous', 'emp_var_rate', 'cons_price_idx', 'cons_conf_idx', 'euribor3m', 'nr_employed', 'y'
cols_to_keep = ['age','duration','campaign', 'pdays', 'previous', 'emp_var_rate', 'cons_price_idx', 'cons_conf_idx', 'euribor3m', 'nr_employed', 'y']
banking_filt = banking[cols_to_keep]
# %% Create X and y
X = banking_filt.drop(['y'], axis=1)
y = banking_filt['y']

#%% Perform Train / Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#%% Set up Model Pipeline with StandardScaler, LogisticRegression
steps = [
    ('scaler', StandardScaler()),
    ('log_reg', LogisticRegression())
]

pipeline = Pipeline(steps)

clf = pipeline.fit(X_train, y_train)


#%% Calculate Predictions on Test data
y_pred = clf.predict(X_test)


#%% Calculate Baseline Classifier
1 - np.sum(y_test) / len(y_test)

#%% Calculate Confusion Matrix on Test data
confusion_matrix(y_true=y_test, y_pred=y_pred)

#%% Compare our Model Accuracy to Baseline Model Accuracy
accuracy_score(y_test, y_pred)
# %%
print(classification_report(y_test, y_pred))
# %%
