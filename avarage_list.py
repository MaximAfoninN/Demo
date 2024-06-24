import logging
import sys

logging.basicConfig(level=logging.INFO, filename="average_list.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s %(funcName)s %(lineno)d")


logging.info(f"Testing the custom logger for module ...")

print("Добавьте список: ")
average_list = []

try:
    average_list = [int(value) for value in input().split()]
except ValueError:
    print("Incorrect symbol added. Please enter only numbers, letters and string are not accepted.")
    logging.error(f"The list of numbers contain strings.")
    logging.error("Incorrect symbol added. Please enter only numbers, letters and string are not accepted.")
    average_list.clear()
    try:
        average_list = [int(value) for value in input().split()]
    except ValueError:
        print("Incorrect symbol. The program will be closed.")
        logging.critical("The second list of numbers contain strings.")
        logging.critical("Incorrect symbol(s). The program will be closed.")
        sys.exit()

try:
    average_number = sum(average_list) / len(average_list)
    print(average_number)
except ZeroDivisionError:
    print("Список не должен быть пустым.")
    logging.error("The list should be empty.")

# average_number = sum(average_list) / len(average_list)

"""print("Please add number to the list: ")
try:
    number = int(input())
except ValueError:
    print("Incorrect symbol added. Please enter only numbers, letters and string are not accepted.")
    print("Please add number to the list: ")
    try:
        number = int(input())
    except ValueError:
        print("Incorrect symbol. The program will be closed.")
        sys.exit()
finally:
    average_list.append(number)
    print(average_list)
"""
