import pandas as pd

countries = pd.read_csv('../data/countries.csv')

alcohol = pd.read_csv('../data/alcohol.csv', quotechar="|", sep=' ')
religion = pd.read_csv('../data/religion.csv', quotechar='|', sep=' ')
prices = pd.read_csv('../data/prices.csv', quotechar='|', sep=' ')

cleanliness = pd.read_csv('../data/cleanliness_final.csv')
safety = pd.read_csv('../data/safety_data_matched.csv')

merge1 = pd.merge(countries, alcohol, how='left', on=['country'])
print(merge1.head())

merge2 = pd.merge(merge1, religion, how='left', on=['country'])
print(merge2.head())

merge3 = pd.merge(merge2, prices, how='left', on=['country'])
print(merge3.head())

merge4 = pd.merge(merge3, cleanliness, how='left', on=['country'])
print(merge4.head())

merge5 = pd.merge(merge4, safety, how='left', on=['country'])
print(merge5.head())

merge5.to_csv('merged.csv', index=False)
