import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

fixed_df = pd.read_csv('data/bikes.csv',  # Это то, куда вы скачали файл
                       sep=';', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True,
                       index_col='Date')
fixed_df[:3]
fixed_df['Berri 1'][:10]
fixed_df[:6]
fixed_df['Berri 1'].plot()
plt.show()
print(fixed_df[:15])