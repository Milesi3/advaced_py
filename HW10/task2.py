# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, side1, side2=None):
        if side2 == None:
            self.side1 = self.side2 = side1
        else:
            self.side1 = side1
            self.side2 = side2

    def perimetr(self):
        return 2 * (self.side1 + self.side2)

    def area(self):
        return self.side1 * self.side2


a = Rectangle(10)
b = Rectangle(10, 5)
print(a.perimetr(), a.area())
print(b.perimetr(), b.area())
