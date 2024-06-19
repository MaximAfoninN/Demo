from random import randint

N = 10  # количество элементов в списке
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)  # вывод исходного неотсортированного списка

# Сама сортировка методом "пузырька"
for i in range(N-1):
    for j in range(N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)  # вывод отсортированного списка