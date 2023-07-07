# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def len_circle(self):
        return math.pi * 2 * self.radius

    def area_circle(self):
        return math.pi * self.radius ** 2

a = Circle(5)
print(Circle.len_circle(a))
print(a.area_circle())