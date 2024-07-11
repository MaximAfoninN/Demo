class LoggedAttributes:
    def __init__(self, attr1, attr2, attr3):
        self._attr1 = attr1
        self._attr2 = attr2
        self._attr3 = attr3

    @property
    def attr1(self):
        return self._attr1

    @attr1.setter
    def attr1(self, value):
        print(f"Атрибут изменен с {self._attr1} на {value}.")
        self._attr1 = value

    @property
    def attr2(self):
        return self._attr2

    @attr2.setter
    def attr2(self, value):
        print(f"Атрибут изменен с {self._attr2} на {value}.")
        self._attr2 = value

    @property
    def attr3(self):
        return self._attr3

    @attr3.setter
    def attr3(self, value):
        print(f"Атрибут изменен с {self._attr3} на {value}.")
        self._attr3 = value


if __name__ == "__main__":
    Attributes = LoggedAttributes(241, "Initial", [4, 5, 67, 46])
    Attributes.attr1 = 'new_value1'
    Attributes.attr2 = 42
    Attributes.attr3 = [1, 2, 3]
