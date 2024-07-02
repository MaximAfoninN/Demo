import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (10, 5)

complaints = pd.read_csv('data/311-service-requests.csv')
# print(complaints['Complaint Type'][:5])
# print(complaints[:5])
# print(complaints[['Complaint Type', 'Borough']])
# print(complaints[['Complaint Type', 'Borough']][:10])
# print(complaints['Complaint Type'].value_counts())
complaint_counts = complaints['Complaint Type'].value_counts()
print(complaint_counts[:10])
complaint_counts[:10].plot(kind='bar')
plt.show()