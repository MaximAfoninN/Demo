from memory_profiler import profile
import cProfile

class Calculator:
    def sum(self, first_input, second_input):
        return first_input + second_input

class StringTotal(Calculator):
    def __add__(self, first_input, second_input):
        return str(first_input) + " " + str(second_input)

@profile
def main():
    # Сумма двух чисел
    print(Calculator().sum(10, 5))

    # Конкатенация двух строк
    string = StringTotal()
    print(string.__add__("Hello", "people"))

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()
    profiler.print_stats(sort='cumtime')
