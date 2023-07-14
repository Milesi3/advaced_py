# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.

from MyBaseException import NegativeMeaning
class Rectangle:
    """Доработанный класс прямоугольник из прошлого семинара."""

    def __init__(self, *args):
        """Инициализация данных"""
        if len(args) == 1:
            self.length = args[0]
            self.width = self.length
        elif len(args) == 2:
            self.length, self.width = args
        else:
            self.length, self.width, _ = args
        if self.length < 0 or self.width < 0:
            raise NegativeMeaning(self.length, self.width)

    def get_perimeter(self):
        return self.length * 2 + self.width * 2

    def get_square(self):
        return self.length * self.width

    def __add__(self, other):
        p = self.get_perimeter() + other.get_perimeter()
        return Rectangle(p // 2 / 2)

    def __sub__(self, other):
        p = self.get_perimeter() - other.get_perimeter()
        return Rectangle(abs(p // 2 / 2))

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        return self.get_square() > other.get_square()

    def __lt__(self, other):
        return self.get_square() < other.get_square()

    def __ge__(self, other):
        return self.get_square() >= other.get_square()

    def __le__(self, other):
        return self.get_square() <= other.get_square()

    def __str__(self):
        return f'Экземпляр класса Rectangle "{self.length}" и "{self.width}"'

    def __repr__(self):
        return f'Rectangle({self.length = }, {self.width = })'


if __name__ == "__main__":
    rec_1 = Rectangle(-5,4)
    rec_2 = Rectangle(5)
    print(f'{rec_1.get_perimeter() = }\n{rec_2.get_perimeter() = }')
    rec_3 = rec_1 + rec_2
    rec_4 = rec_1 - rec_2
    print(f'{rec_3.length = }\n{rec_3.width = }')
    print(f'{rec_4.length = }\n{rec_4.width = }')
    print(rec_1 == rec_2)
    print(rec_3 <= rec_4)
