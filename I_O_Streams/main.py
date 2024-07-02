import pathlib
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Рисовать графики сразу же
# %matplotlib inline

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

# Получаем строку, содержащую путь к рабочей директории:
work_path = pathlib.Path.cwd()

# сохраним путь к csv файлу в переменной data_path,
data_path = Path(work_path, 'datasets', 'bikes.csv')

# Загружаем данные из csv файла в переменную data ks-projects-201612.csv"
data = pd.read_csv(data_path)
var = data[:3]
data['Berri 1'].plot()
plt.show()

data.head(10)

# fixed_df = pd.read_csv('bikes.csv',  # Это то, куда вы скачали файл
#                       sep=';', encoding='latin1',
#                       parse_dates=['Date'], dayfirst=True,
#                       index_col='Date')
# fixed_df[:3]

# print(work_path)
# print(data_path)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
