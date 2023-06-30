# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из предыдущей задачи.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv


def convert_pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)

    if isinstance(data, dict):
        data = [data]

    column_headers = set()
    for dictionary in data:
        column_headers.update(dictionary.keys())

    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=column_headers)
        writer.writeheader()
        writer.writerows(data)


data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}
with open('input.pickle', 'wb') as f:
    pickle.dump(data, f)


pickle_file_path = 'input.pickle'
csv_file_path = 'output.csv'

convert_pickle_to_csv(pickle_file_path, csv_file_path)
