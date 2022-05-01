import pandas as pd

safety = pd.read_csv('../data/safety_data.txt', delimiter='\t')
countries = pd.read_csv('../data/countries.csv')

safety.drop('id', inplace=True, axis=1)
safety.to_csv('safety_data_matched.csv', index=None)
