import abc


class Animals(abc.ABC):
    @abc.abstractmethod
    def voice(self):
        pass


class Cat(Animals):
    def voice(self):
        return "Мяу"


cat = Cat()
print(cat.voice())
