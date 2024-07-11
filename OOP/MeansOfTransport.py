class MeansOfTransport:

    def __init__(self, color, brand):
        print("Init method")
        self.__color = color
        self.__brand = brand

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    # Setter метод
    # def set_color_brand(self, color, brand):
    #    self.__color = color
    #    self.__brand = brand

    # Getter метод
    # def get_color_brand(self):
    #    return self.__color, self.__brand

    def show_color(self, __color):
        self.color = __color
        print("The color of : " + __color)

    def show_brand(self, __brand):
        self.brand = __brand
        print("The brand : " + __brand)


car1 = MeansOfTransport("Yellow", "Toyota")
print(car1.__dict__)
car1.color = "Red"
car1.brand = "Audi"
print("Color of car : " + car1.color, ".  Brand of car: " + car1.brand)


# car1.show_color()
# car1.show_brand()
# car1.set_color_brand("Black", "Audi") # Использование метода сетер
# print(car1.get_color_brand()) # B # Использование метода гетер
# print(car1.__color, car1.__brand)


class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, number_of_wheels, color, brand, engine_type, weight):
        super().__init__(color, brand)
        self.__number_of_wheels = number_of_wheels
        self._engine_type = engine_type
        self.__weight = weight

    @classmethod
    def show_car_drive(cls):
        print(cls.car_drive)

    @property
    def number_of_wheels(self):
        return self.__number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, number_of_wheels):
        self.__number_of_wheels = number_of_wheels

    def __del__(self):
        print("Удаление экземпляра: " + str(self))

    # Метод класса __call__. Экземпляры класса можно вызывать, как функции
    def __call__(self, *args, **kwargs):
        print("__call__")

    # __rpr__ Вывод отладочной информации
    def __repr__(self):
        return f"{self.__class__}: {self.brand}"

    # __str__ Вывод  информации для пользователя
    def __str__(self):
        return f"{self.brand}"

    # __len__ D Возвращает длину объекта
    def __len__(self):
        return len(self.brand)

    # Возвращает модуль числа
    def __abs__(self):
        return self.__weight


class Moped(MeansOfTransport):
    def __init__(self, number_of_wheels, color, brand):
        super().__init__(color, brand)
        self.__number_of_wheels = number_of_wheels

    @staticmethod
    def time(speed, distance):
        return distance / speed


print(Moped.time(100, 1000))
car1 = Car(4, "red", "Audi", "Diesel", "2000")
# print(car1.__dict__)

# Доступ к переменным protected и private
# print(car1.__weight)
# print(car1._engine_type)

# Вывод переменной класса car_drive
print("Вывод переменной класса car_drive: ")
Car.show_car_drive()

# Метод класса __call__. Экземпляры класса можно вызывать, как функции
car1()

# Магически методы __str__, __repr__, __len__, __abs__
print(car1) # __str__ Вывод  информации для пользователя
print(car1) # __rpr__ Вывод отладочной информации
print(len(car1)) # __len__ D Возвращает длину объекта
print(abs(car1)) # Возвращает модуль числа

# Магически методы __add__, __sub__, __mul__, __truediv__