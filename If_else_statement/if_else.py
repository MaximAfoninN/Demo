# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("")

# Three integers are given. Find the number of positive numbers in the original set.
print("Даны три целых числа. Найти количество положительных чисел в исходном наборе.")


def if_number_positive(a):
    positive_sum = 0
    if a > 0:
        positive_sum = positive_sum + 1
    return positive_sum


first_number = int(input("Введите первое число : "))
sum = if_number_positive(first_number)
second_number = int(input("Введите второе число : "))
sum = if_number_positive(second_number) + sum
third_number = int(input("Введите третье число : "))
sum = if_number_positive(third_number) + sum
print(f"Вы ввели {sum} положительных чисел")
print()

# Two numbers are given. Output the largest of them.
print("Two numbers are given. Output the largest of them.")
first_number = int(input("Please enter first number : "))
second_number = int(input("Please enter second number : "))
if first_number > second_number:
    print(f"The largest number is: {first_number}")
else:
    print(f"The largest number is: {second_number}")
print()

# Two numbers are given. Print first the larger one and then the smaller one.
print("Two numbers are given. Print first the larger one and then the smaller one.")
first_number = int(input("Please enter first number : "))
second_number = int(input("Please enter second number : "))
if first_number > second_number:
    print(f"{first_number} , {second_number}")
else:
    print(f"{second_number} , {first_number}")
print()

# Three numbers are given. Find the smallest of them.
smallest_number = 0
print("Three numbers are given. Find the smallest of them.")
first_number = int(input("Please enter first number : "))
second_number = int(input("Please enter second number : "))
third_number = int(input("Please enter first number : "))
if first_number < second_number and first_number < third_number:
    smallest_number = first_number
elif second_number < first_number and second_number < third_number:
    smallest_number = second_number
else:
    smallest_number = third_number
print(f"The smallest number is : {smallest_number}.")
print()

# Determine the number of the coordinate quarter in which the point is located.
print("# Determine the number of the coordinate quarter in which the point is located.")
x = int(input("Please enter x-coordinate of the point : "))
y = int(input("Please enter y-coordinate of the point : "))
if x > 0 and y > 0:
    print(f"The point is located in 1-nd quadrant ({x} , {y})")
elif x < 0 < y:
    print(f"The point is located in 2-nd quadrant ({x} , {y})")
elif x < 0 and y < 0:
    print(f"The point is located in 3-nd quadrant ({x} , {y})")
elif x > 0 > y:
    print(f"The point is located in 4-nd quadrant ({x} , {y})")
else:
    print(f"The point is located at Zero coordinates ({x} , {y})")
