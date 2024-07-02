import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

requests = pd.read_csv('data/311-service-requests.csv')
# print(requests['Incident Zip'].unique())
na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('data/311-service-requests.csv', na_values=na_values, dtype={'Incident Zip': str})
# print(requests['Incident Zip'].unique())
rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
len(requests[rows_with_dashes])
requests[rows_with_dashes]['Incident Zip']
long_zip_codes = requests['Incident Zip'].str.len() > 5
requests['Incident Zip'][long_zip_codes].unique()
zero_zips = requests['Incident Zip'] == '00000'
requests.loc[zero_zips, 'Incident Zip'] = np.nan
unique_zips = requests['Incident Zip'].unique()
unique_zips
zips = requests['Incident Zip']
is_close = zips.str.startswith('0') | zips.str.startswith('1')
is_far = ~(is_close) & zips.notnull()
zips[is_far]
requests[is_far][['Incident Zip', 'Descriptor', 'City']].sort_values('Incident Zip')
print(requests['City'].str.upper().value_counts())