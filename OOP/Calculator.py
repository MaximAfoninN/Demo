import cProfile


class Calculator:
    #@staticmethod
    def sum(first_input, second_input):
        return first_input + second_input


class StringTotal(Calculator):
    def __add__(self, first_input, second_input):
        return str(first_input) + " " + str(second_input)


# Cуммa двух чисел

print(Calculator.sum(10, 5))

# Конкатенация двух строк
string = StringTotal()
print(string.__add__("Hello", "people"))

