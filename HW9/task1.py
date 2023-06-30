# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


# Существует проблема, что декоратор работает над старым файлом, и только после обработки корней создается новый файл.
# Пришлось делать костыль в виде функции process_csv,
# так как возникала ошибка, если я передавал декораторы прямо на csv_gen.
# Также не смог решить проблему передачи результата в json, он просто не передается

import csv
import math
import random
import json


def save_results_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        parameters = {
            'args': args,
            'kwargs': kwargs
        }
        save_to_json(parameters, result)
        return result

    return wrapper


def save_to_json(parameters, result):
    data = {
        'parameters': parameters,
        'result': result
    }
    with open('results.json', 'w') as file:
        json.dump(data, file)
        file.write('\n')
        file.close()


def quadratic_equation_decorator(func):
    def wrapper(*args, **kwargs):
        with open('data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            koren_2(reader)
        return func(*args, **kwargs)

    return wrapper


def koren_2(reader):
    results = []
    for row in reader:
        a, b, c = map(int, row)
        d = b ** 2 - 4 * a * c
        if d < 0:
            results.append("No real roots")
            print("No real roots")
        elif d == 0:
            root = -b / (2.0 * a)
            results.append(f"Single real root: {root}")
            print(f"Single real root: {root}")
        else:
            root1 = (-b + math.sqrt(d)) / (2.0 * a)
            root2 = (-b - math.sqrt(d)) / (2.0 * a)
            results.append(f"Two real roots: {root1}, {root2}")
            print(f"Two real roots: {root1}, {root2}")
    return results


def csv_gen(count=100, name_csv='data.csv'):
    with open(name_csv, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)
        for _ in range(count):
            filewriter.writerow([random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000)])


csv_gen()


@save_results_decorator
@quadratic_equation_decorator
def process_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        koren_2(reader)


process_csv('data.csv')
