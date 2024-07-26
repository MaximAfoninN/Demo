def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1

# Использование генератора
counter = count_up_to(7)
for num in counter:
    print(num)  # Выводит числа от 1 до 5


# Генераторное выражение
squares = (x * x for x in range(10))

# Использование генератора
for square in squares:
    print(square)  # Выводит квадраты чисел от 0 до 9



class CountUpTo:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# Использование итератора
counter = CountUpTo(5)
for num in counter:
    print(num)  # Выводит числа от 1 до 5
