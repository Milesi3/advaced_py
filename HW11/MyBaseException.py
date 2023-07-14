class MyBaseException(Exception):
    pass


class NegativeMeaning(MyBaseException):

    def __init__(self, length, width):
        self.length, self.width = length, width

    def __str__(self):
        return f"Какое-то из значений {self.length = } или {self.width = } меньше 0. Вводите положительные числа!"
