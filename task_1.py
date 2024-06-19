import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def p_square(a):
    return a * 4


def s_square(a):
    return a * a


def p_rectangle(a, b):
    return 2 * (a + b)


def s_rectangle(a, b):
    return a * b


def l_circle(d):
    return 3.14 * d


def v_cube(a):
    return a * a * a


def s_cube(a):
    return 6 * (a * a)


def v_parallelepiped(a, b, c):
    return a * b * c


def s_parallelepiped(a, b, c):
    return 2 * (a * b + b * c + a * c)


def l2_circle(r):
    p = 3.14
    return p * r * 2


def s_circle(r):
    p = 3.14
    return p * r ** 2


def average(a, b):
    return (a + b) / 2


def geometric_average(a, b):
    return math.sqrt(abs(a) * abs(b))


def positive_numbers_sum(result):
    summary = (a ** 2) + (b ** 2)
    return summary


def positive_numbers_difference(a, b):
    return (a ** 2) - (b ** 2)


def positive_numbers_multiplication(a, b):
    return (a ** 2) * (b ** 2)


def positive_numbers_division(a, b):
    return (a ** 2) / (b ** 2)


if __name__ == '__main__':
    a = float(input('Введите сторону квадрата a: '))
    print("Периметр квадрата : ", p_square(a))
    print("Площадь квадрата : ", s_square(a))
    a = float(input('Введите сторону прямоугольника a: '))
    b = float(input('Введите вторую сторону прямоугольника b: '))
    print("Периметр прямоугольника : ", p_rectangle(a, b))
    print("Площадь прямоугольника : ", s_rectangle(a, b))
    d = float(input('Введите диаметр круга D: '))
    print("Длина окружности : ", l_circle(d))
    a = float(input('Введите длину ребра куба a: '))
    print("Объем куба V : ", v_cube(a))
    print("Площадь поверхности куба S  : ", s_cube(a))
    a = float(input('Введите сторону параллелепипеда a: '))
    b = float(input('Введите вторую сторону параллелепипеда b: '))
    c = float(input('Введите третью сторону параллелепипеда c: '))
    print("Объем параллелепипеда V : ", v_parallelepiped(a, b, c))
    print("Площадь поверхности параллелепипеда S : ", s_parallelepiped(a, b, c))
    r = float(input('Введите радиус круга R: '))
    print("Длина окружности L : ", l2_circle(r))
    print("Площадь круга S : ", s_circle(r))
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    print("Среднее арифметическое чисел : ", average(a, b))
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    print("Среднее геометрическое чисел : ", geometric_average(a, b))
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    print("Сумма их квадратов : ", positive_numbers_sum(result=sum))
    print("Разность их квадратов : ", positive_numbers_difference(a, b))
    print("Произведение их квадратов : ", positive_numbers_multiplication(a, b))
    print("Частное их квадратов : ", positive_numbers_division(a, b))
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
