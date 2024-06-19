def if_number_positive(a):
    return a > 0


def if_number_odd(a):
    return a % 2 != 0


def if_number_even(a):
    return a % 2 == 0


def compare_2_numbers(a, b):
    return a > 2 and b <= 3


def compare_2_numbers_2(a, b):
    return a >= 0 and b < -2


def compare_3_numbers(a, b, c):
    return a < b < c


def compare_3_numbers_unknown_position(a, b, c):
    return a < b < c or c < b < a


def if_2_number_both_odd(a, b):
    return a % 2 != 0 and b % 2 != 0


def if_2_number_one_odd(a, b):
    return a % 2 != 0 or b % 2 != 0


def if_2_number_only_one_odd(a, b):
    return (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0)


a = int(input("Введите число А : "))
print("Это число положительное : ", if_number_positive(a))

a = int(input("Введите число А : "))
print("Это число нечётное : ", if_number_odd(a))

a = int(input("Введите число А : "))
print("Это число четное : ", if_number_even(a))

print("Выражение A > 2 и B ≤ 3")
a = int(input("Введите число А : "))
b = int(input("Введите число B : "))
print("Выражение A > 2 и B ≤ 3 : ", compare_2_numbers(a, b))

print("Выражение A ≥ 0 или B < −2")
a = int(input("Введите число А : "))
b = int(input("Введите число B : "))
print("Выражение A ≥ 0 или B < −2 : ", compare_2_numbers_2(a, b))

print("Выражение A < B < C")
a = int(input("Введите число А : "))
b = int(input("Введите число B : "))
c = int(input("Введите число C : "))
print("Выражение A < B < C : ", compare_3_numbers(a, b, c))

print("Выражение A < B < C или С < B < A")
a = int(input("Введите число А : "))
b = int(input("Введите число B : "))
c = int(input("Введите число C : "))
print("Выражение A < B < C : ", compare_3_numbers_unknown_position(a, b, c))

print("Числа A и B нечетные.")
a = int(input("Введите число А : "))
b = int(input("Введите число B : "))
print("Числа A и B нечетные : ", if_2_number_both_odd(a, b))

print("Числа A или B нечетные.")
a = int(input("Введите число А : "))
b = int(input("Введите число B : "))
print("Числа A или B нечетные : ", if_2_number_one_odd(a, b))

print("Только одно число A или B нечетное.")
a = int(input("Введите число А : "))
b = int(input("Введите число B : "))
print("Числа A и B нечетные : ", if_2_number_only_one_odd(a, b))
