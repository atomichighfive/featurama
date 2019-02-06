#%%
import pandas as pd
import dask.dataframe as dd
from featurama.interactions.numeric import pairwise

#%%
data = dd.read_csv('./featurama/sample_data/titanic.csv')
data.head()

#%%
ints = pairwise(data, operation = 'all')

ints

ints.compute()
