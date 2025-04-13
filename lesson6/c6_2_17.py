import abc


class Person(metaclass=abc.ABCMeta):
    def __init__(self, age):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError


adult = Adult()
