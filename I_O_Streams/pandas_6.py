import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

# Read it, and remove the last row
popcon = pd.read_csv('data/popularity-contest.csv', sep=' ')[:-1]
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']
popcon['atime'] = popcon['atime'].astype(int)
popcon['ctime'] = popcon['ctime'].astype(int)
popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')
popcon['atime'].dtype
popcon[:5]
popcon = popcon[popcon['atime'] > '1970-01-01']
nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]
print(nonlibraries.sort_values('ctime', ascending=False)[:10])
