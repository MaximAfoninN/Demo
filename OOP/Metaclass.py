
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Создаем новый класс
        dct['my_attribute'] = 42
        return super().__new__(cls, name, bases, dct)

# Используем метакласс для создания класса
class MyClass(metaclass=MyMeta):
    pass

# Создаем экземпляр класса
instance = MyClass()
print(instance.my_attribute)  # 42
