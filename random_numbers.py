import logging
import random

# получение пользовательского логгера и установка уровня логирования
random_logger = logging.getLogger(__name__)
random_logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика в соответствии с нашими нуждами
random_handler = logging.FileHandler(f"random_numbers.log", mode='w')
random_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s %(funcName)s %(lineno)d")

# добавление форматировщика к обработчику
random_handler.setFormatter(random_formatter)
# добавление обработчика к логгеру
random_logger.addHandler(random_handler)

random_logger.info(f"Testing the custom logger for module {__name__}...")

print("Генерация случайных чисел в заданном диапазоне.")
begin = int(input("Введите начальную границу диапазона : "))
end = int(input("Введите конечную границу диапазона : "))
try:
    x = [random.randint(begin, end) for i in range(10)]
    print(x)
except ValueError:
    print()
    print("Конечная граница должна быть больше начальной.")
    random_logger.error(f"The final boundary must be greater than the initial one. Begin ({begin}) must be greater than end ({end}).")
    begin = int(input("Введите начальную границу диапазона : "))
    end = int(input("Введите конечную границу диапазона : "))
    try:
        x = [random.randint(begin, end) for i in range(10)]
        print(x)
    except ValueError:
        random_logger.error(f"The final boundary must be greater than the initial one. Begin ({begin}) must be greater than end ({end}).")
        print("Вы два раза ввели неправильное значение. Программа остановлена.")
