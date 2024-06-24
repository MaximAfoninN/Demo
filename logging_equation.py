import logging
import math
import sys

logging.basicConfig(level=logging.INFO, filename="logging_equation.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s %(funcName)s %(lineno)d")


#def get_coeficents():
#    a = int(input("Введите a: "))
#    b = int(input("Введите b: "))
#    c = int(input("Введите c: "))
#    return a, b, c


#def find_discriminant(a: int, b: int, c: int) -> int:
#   return b ** 2 - 4 * a * c


def solve(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    logging.info(f"Discriminant : {discriminant}")
    try:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        logging.info(f"The first root:  {root1}, the second root: {root2}.")
    except ValueError:
        logging.error(f"Discriminant negative. Please enter another a,b,c : ")
        print("Discriminant negative. Please enter another a,b,c : ")
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        c = float(input("Введите c: "))
        try:
            discriminant = b ** 2 - 4 * a * c
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            logging.info(f"The first root:  {root1}, the second root: {root2}.")
        except ValueError:
            logging.error(f"Discriminant still negative. The program will be closed.")
            print("Discriminant still negative. The program will be closed.")
            sys.exit()
    return root1, root2


a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
logging.info(f"A = {a}, B = {b}, C = {c}")

try:
    root1, root2 = solve(a, b, c)
    print(f"The roots of the equation are {root1} and {root2}")
except UnboundLocalError:
    print("")

""""
try:
    Discriminant = math.sqrt(find_discriminant(a, b, c))
except ValueError:
    print("Дискриминант отрицательный. У уравнения 0 корней. Пожалуйста введите другие a,b,c : ")



print("Решения квадратного уравнения ax^2 + bx + c = 0.")

logging.info(f"The values of a, b, c are {a} , {b} and {c}")


try:
    D = b ** 2 - 4 * a * c
    logging.info(f"x/y successfuly divided with result: {D}")
except ZeroDivisionError as err:
    logging.info("Zero division error", exc_info=True)
"""
