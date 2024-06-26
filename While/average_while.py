print("Введите число: ")
i = int(input())
a = 0
sum = 0
while i != 0:
    print("Введите число: ")
    sum = i + sum
    i = int(input())
    a = a + 1
try:
    avg = sum / a
    print(f"Среднее этих чисел :  {avg=}")
except ZeroDivisionError:
    print("Среднее : 0")

