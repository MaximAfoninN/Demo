import abc


class Dog:
    __instance__ = None

    def __init__(self, name, breed, age, weight):
        # This is a Constructor
        if Dog.__instance__ is None:
            Dog.__instance__ = self
        else:
            raise Exception("We can not creat another class")
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight

    @staticmethod
    def get_instance():
        # We define the static method to fetch instance
        if not Dog.__instance__:
            Dog()
        return Dog.__instance__


    def voice(self):
        return "Гав"

    @abc.abstractmethod
    def movement(self):
        pass



Dog1 = Dog("Lord", "Овчарка", 4, 40)
print(Dog1)

Dog2 = Dog.get_instance()
print(Dog2)

Dog3 = Dog.get_instance()
print(Dog3)