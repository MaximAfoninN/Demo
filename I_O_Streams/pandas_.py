# Подключаем библиотеку Pandas
import pandas as pd

# подключаем модуль pathlib и библиотеку Path модуля pathlib
import pathlib
from pathlib import Path

# Получаем строку, содержащую путь к рабочей директории:
work_path = pathlib.Path.cwd()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# сохраним путь к csv файлу в переменной data_path
data_path = Path(work_path, 'datasets', 'bikes.csv')

# Загружаем данные из csv файла в переменную data
# data = pd.read_csv(data_path, nrows=3)
data = pd.read_csv(data_path, usecols = ["Rachel1"])

print("Average = ", data["Rachel1"].mean())
print("Minimun = ", data["Rachel1"].min())
print("Maximum = ", data["Rachel1"].max())
print("Median = ", data["Rachel1"].median())

# Выведем первые 10 строк из прочитанного файла на экран
# print(data)
