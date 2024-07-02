import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (10, 5)

"""bikes = pd.read_csv('data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
bikes['Berri 1'].plot()
# plt.show()
berri_bikes = bikes[['Berri 1']].copy()
# print(berri_bikes[:5])
# print(berri_bikes.index)
# print(berri_bikes.index.day)
print(berri_bikes.index.weekday)
berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday
# print(berri_bikes[:5])
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
print(weekday_counts)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekday_counts)
print(weekday_counts.plot(kind='bar'))
plt.show()"""

bikes = pd.read_csv('data/bikes.csv',
                    sep=';', encoding='latin1',
                    parse_dates=['Date'], dayfirst=True,
                    index_col='Date')
# Add the weekday column
berri_bikes = bikes[['Berri 1']].copy()
berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday

# Add up the number of cyclists by weekday, and plot!
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts.plot(kind='bar')
plt.show()
