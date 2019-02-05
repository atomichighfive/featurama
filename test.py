#%%
import pandas as pd
import dask.dataframe as dd
from featurama.interactions.numeric import pairwise

#%%
data = dd.read_csv('./titanic.csv')
data.head()

#%%
ints = pairwise(data, operation = 'all')

ints

ints.compute()
