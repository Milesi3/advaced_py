# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            size = os.path.getsize(file_path)
            results.append({
                'type': 'file',
                'path': file_path,
                'parent_directory': root,
                'size': size
            })

        for name in dirs:
            dir_path = os.path.join(root, name)
            size = get_directory_size(dir_path)
            results.append({
                'type': 'directory',
                'path': dir_path,
                'parent_directory': root,
                'size': size
            })

    return results


def get_directory_size(directory):
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for f in files:
            file_path = os.path.join(root, f)
            total_size += os.path.getsize(file_path)

    return total_size


def save_results(results, file_path):

    with open(f"{file_path}.json", 'w') as f:
        json.dump(results, f, indent=4)

    with open(f"{file_path}.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['type', 'path', 'parent_directory', 'size'])
        writer.writeheader()
        writer.writerows(results)

    with open(f"{file_path}.pickle", 'wb') as f:
        pickle.dump(results, f)


directory = r'C:\Users\irina\Desktop\GB\advanced_python\HW7'
results = traverse_directory(directory)

file_path = 'output'

save_results(results, file_path)

