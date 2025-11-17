from Section import Section
class Person:
    __section=set()

    def add_section(self, value):
        if isinstance(value, Section):
            self.__section.add(value)

    def del_section(self, section_name):
        for i in self.__section:
            if i.name == section_name:
                self.__section.discard(name)
                break


    def __init__(self, fio, phone):
        self.__fio = fio
        self.__phone = phone

    def __str__(self):
        if self.__section:
            return (f"fio: {self.__fio} | phone: {self.__phone} | {self.__section}")
        else:
            return (f"fio: {self.__fio} | phone: {self.__phone}")


    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, value):
        self.__fio = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value


if __name__ == '__main__':
    person = Person("fio", "5232352352")
    person.phone=41241241
    box = Section("Бокс", 25)
    print(box)
    person.add_section(box)
    print(person)

