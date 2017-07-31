import pandas as pd
import numpy as np


train_data  = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
profiles = pd.read_csv("profiles.csv")

profiles.ix[profiles['sex'].isnull(),'sex'] = 'a'

profiles.ix[profiles['age'].isnull(),'age'] = np.nanmean(profiles['age'])

train = pd.merge(train_data, profiles, how='inner', on='user')
test = pd.merge(test_data, profiles, how='inner', on='user')
train.to_csv('train1.csv', index = False)
test.to_csv('test1.csv', index = False)