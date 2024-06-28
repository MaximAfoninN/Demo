# Given an integer K. Print a line describing the estimate corresponding to the number K.
import sys

print("Given an integer K. Print a line describing the estimate corresponding to the number K.")
print()

K = int(input("Enter grade: "))

match K:
    case 1:
        print("Bad grade.")
    case 2:
        print("Unsatisfactory grade.")
    case 3:
        print("Satisfactory grade.")
    case 4:
        print("Good grade.")
    case 5:
        print("Excellent grade.")
    case _:
        print("Incorrect input.")

# Determine the number of days in this month for a non-leap year.
print()
print("Determine the number of days in this month for a non-leap year.")

M = int(input("Enter number of the month: "))

match M:
    case 1:
        print("January: 31 days.")
    case 2:
        print("February: 28 days.")
    case 3:
        print("March: 31 days.")
    case 4:
        print("April: 30 days.")
    case 5:
        print("May: 31 days")
    case 6:
        print("June: 30 days.")
    case 7:
        print("July: 31 days.")
    case 8:
        print("August: 31 days.")
    case 9:
        print("September: 30 days.")
    case 10:
        print("October: 31 days")
    case 11:
        print("November: 30 days.")
    case 12:
        print("December: 31 days")
    case _:
        print("Incorrect input.")

# Print the values of D and M for the date following the specified one.
print()
print("Print the values of the D and M for the date following the specified one.")
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
M = int(input("Enter month: "))
D = int(input("Enter day: "))
match D:
    case day if day < days_in_month[M - 1]:
        D += 1
    case _:
        D = 1
        match M:
            case 12:
                M = 1
            case _:
                M += 1
print(f"The month: {M} , the day: {D}")
print()

# Print the direction of the robot after executing the received command.
print("Print the direction of the robot after executing the received command.")
C = input("Enter the initial direction of the robot (N, E, S, W): ").strip().upper()
N = int(input("Enter the command sent to the robot: 0 — continue moving, 1 — turn left, −1 — turn right "))
directions = ["N", "E", "S", "W"]
direction_index = directions.index(C)
match N:
    case 0:
        new_direction = C
    case 1:
        new_direction = directions[direction_index - 1]
    case -1:
        new_direction = directions[(direction_index + 1) % 4]
    case _:
        raise ValueError("Invalid command. Must be 0, 1, -1")
print(f"The new direction is : {new_direction}")

# Print a line describing this number.
print()
print("Print a line describing this number,")
ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
teens = ["", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать",
         "восемнадцать", "девятнадцать"]
tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
        "девяносто"]
hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
number = int(input("Введите число on 100 до 999 : "))
if not (100 <= number <= 999):
    print("Number out of range")
    sys.exit()
hundred = number // 100
remainder = number % 100
ten = remainder // 10
one = remainder % 10
# print(hundred)
# print(remainder)
# print(ten)
# print(one)

words = hundreds[hundred]
match remainder:
    case 0:
        words
    case _ if 1 <= remainder <= 9:
        words += " " + ones[remainder]
    case _ if 11 <= remainder <= 19:
        words += " " + teens[remainder - 10]
    case _:
        words += " " + tens[ten]
        if one > 0:
            words += " " + ones[one]
print(words)
