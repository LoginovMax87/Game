class Section:

    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    def __str__(self):
        return (f"name: {self.__name} | quantity: {self.__quantity}")


if __name__ == '__main__':
    box = Section("Бокс", 25)
    print(box)