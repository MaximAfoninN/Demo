def find_full_meter(l):
    return l // 100


def find_full_tons(kg):
    return kg // 1000


def find_full_kilobytes(file_size):
    return file_size // 1024


def find_number_line(full_line, short_line):
    return full_line // short_line


def find_empty_line(full_line, short_line):
    return full_line % short_line


def find_place_numbers(number):
    tens = number // 10
    ones = number % 10
    return tens, ones


def sum_mult_numbers(tens, ones):
    sum = tens + ones
    mult = tens * ones
    return sum, mult


def change_number_position(tens, ones):
    temp = tens
    tens = ones
    ones = temp
    return tens, ones


def find_place_3_numbers(number):
    hundreds = number // 100
    return hundreds


def find_two_last_in_3numbers(number):
    two_number = number % 100
    return two_number

l = int(input("Введите расстояние в сантиметрах : "))
print("Полных метров : ", find_full_meter(l), "метра")

kg = int(input("Введите массу в килограммах : "))
print("Полных тонн : ", find_full_tons(kg), "тонны")

file_size = int(input("Введите объем файла в байтах : "))
print("Размер файла ", find_full_kilobytes(file_size), " килобайт")

full_line = int(input("Введите длину отрезка А : "))
short_line = int(input("Введите длину отрезка B (должен быть меньше А) : "))
print("Кол-во отрезков B в А : ", find_number_line(full_line, short_line))

full_line = int(input("Введите длину отрезка А : "))
short_line = int(input("Введите длину отрезка B (должен быть меньше А) : "))
print("Длина незанятой части А : ", find_empty_line(full_line, short_line))

number = int(input("Введите двузначное число : "))
tens, ones = find_place_numbers(number)
print("Десятки : ", tens, "Единицы : ", ones)

number = int(input("Введите двузначное число : "))
tens, ones = find_place_numbers(number)
print("Десятки : ", tens, "Единицы : ", ones)
sum, mult = sum_mult_numbers(tens, ones)
print("Суммы чисел : ", sum, "Произведение чисел : ", mult)

number = int(input("Введите двузначное число : "))
tens, ones = find_place_numbers(number)
print("Десятки : ", tens, "Единицы : ", ones)
tens, ones = change_number_position(tens, ones)
print("Число после перестановки места : ", tens, ones)

number = int(input("Введите трехзначное число : "))
print("Первая цифра числа :", find_place_3_numbers(number))

number = int(input("Введите трехзначное число : "))
print("Двузначное число : ", find_two_last_in_3numbers(number))
double_digit_number = find_two_last_in_3numbers(number)
tens, ones = find_place_numbers(double_digit_number)
tens, ones = change_number_position(tens, ones)
print("Двузначное число после перестановки места : ", tens, ones)