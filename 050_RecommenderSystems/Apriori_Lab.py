# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Packages

# %%
# Data Manipulation
import pandas as pd
import numpy as np

# Modeling
from mlxtend.frequent_patterns import apriori, association_rules 

# Visualisation
from plotnine import ggplot, aes, theme, geom_col, element_text

# %%  Data Preparation
# open the file and import all transactions

retail = pd.read_excel("./data/OnlineRetail.xls")
retail.head()
# %%
retail.columns

# %% Data Cleaning
# stripping extra spaces in the description
retail['Description'] = retail['Description'].str.strip()


# %%
retail.shape


# %%
# Dropping the rows without any invoice number 
retail.dropna(subset =['InvoiceNo'], axis = 0, inplace = True) 
retail['InvoiceNo'] = retail['InvoiceNo'].astype('str') 
retail.shape

# %%  Modeling
# Create a basket (sparse matrix with transactions x items)

# %%
basket_germany = (retail[retail['Country'] == 'Germany']
 .groupby(['InvoiceNo', 'Description'])['Quantity']
 .sum()
 .unstack()
 .reset_index()
 .fillna(0)
 .set_index('InvoiceNo')
)


# %%
basket_germany

# %% One-Hot Encoding

# %%
def hot_encode(x): 
    if(x<= 0): 
        return 0
    if(x>= 1): 
        return 1

# %% [markdown]
# *applymap()* applies a function elementwise to every element of a dataframe.

# %%
basket_germany = basket_germany.applymap(hot_encode)
basket_germany


# %%
freq_items = pd.DataFrame(apriori(basket_germany, min_support=0.05, use_colnames=True)).sort_values('support', ascending=False)


# %%
(ggplot(data=freq_items[:40], mapping=aes(x='itemsets', y='support')) +
 geom_col() +
 theme(axis_text_x=element_text(rotation=90, hjust=1))
)


# %%
rules = association_rules(freq_items, metric='lift', min_threshold=1)
rules

# %% [markdown]
# Task: find all itemsets that have 
# - at least two items,
# 
# - a support of 10 %

# %%
freq_items['length'] = freq_items['itemsets'].apply(lambda x: len(x))


# %%
freq_items[(freq_items['length'] >= 2) &
          (freq_items['support'] >= 0.1)
          ]

