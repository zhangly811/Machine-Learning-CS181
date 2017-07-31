import pandas as pd
import numpy as np


train_data  = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
profiles = pd.read_csv("profiles.csv")

# assign third category to sex
profiles.ix[profiles['sex'].isnull(),'sex'] = 'a'
# abnormal age
ind = (profiles['age']<=0) | (profiles['age']>100)
profiles.ix[ind,'age'] = np.nan

country_list = np.array(list(set(profiles['country'])))

age_sex_country = []
for i in range(len(country_list)):
    indf = (profiles['country']==country_list[i]) & (profiles['sex'] == 'f')
    age_f = np.nanmean(profiles.ix[indf,'age'])
    indm = (profiles['country']==country_list[i]) & (profiles['sex'] == 'm')
    age_m = np.nanmean(profiles.ix[indm,'age'])
    inda = (profiles['country']==country_list[i]) & (profiles['sex'] == 'a')
    age_a = np.nanmean(profiles.ix[inda,'age'])
    age_sex_country.append([age_f, age_m, age_a])
age_sex_country = np.array(age_sex_country)

missing_age = profiles['age'].isnull()
for i in range(len(country_list)):
    indf = (profiles['country']==country_list[i]) & (profiles['sex'] == 'f') & missing_age
    profiles.ix[indf,'age'] = age_sex_country[i,0]
    indm = (profiles['country']==country_list[i]) & (profiles['sex'] == 'm') & missing_age
    profiles.ix[indm,'age'] = age_sex_country[i,1]
    inda = (profiles['country']==country_list[i]) & (profiles['sex'] == 'a') & missing_age
    profiles.ix[inda,'age'] = age_sex_country[i,2]

ind = profiles['age'].isnull()
profiles.ix[ind,'age'] = np.nanmean(profiles['age'])

train = pd.merge(train_data, profiles, how='inner', on='user')
test = pd.merge(test_data, profiles, how='inner', on='user')
train.to_csv('train2.csv', index = False)
test.to_csv('test2.csv', index = False)