from accessify import private, protected


class Point:
    def __init__(self, x=0, y=0):
        self.x = self.y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами.")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 5)
pt.set_coord(10, 20)
print(dir(pt))
print(pt._Point__x)

print(pt.get_coord())
