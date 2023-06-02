def check_triangle(a, b, c):
    # Проверка условия существования треугольника
    if a < b + c and b < a + c and c < a + b:
        # Определение типа треугольника
        if a == b == c:
            return "Треугольник является равносторонним."
        if a == b or a == c or b == c:
            return "Треугольник является равнобедренным."

        return "Треугольник является разносторонним."

    return "Треугольник с такими сторонами не существует."

a = 5
b = 4
c = 6
result = check_triangle(a, b, c)
print(result)
