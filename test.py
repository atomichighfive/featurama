#%%
import pandas as pd
from featurama.interactions.numeric import pairwise

#%%
data = pd.read_csv('./../video-game-sales-with-ratings.zip')
data.sample(3)


#%%
ints = pairwise(data, operation = ['sum', 'log'])

display(ints.sample(3))
print(ints.describe)
print(ints.shape)

#%%
import os
os.getcwd()
