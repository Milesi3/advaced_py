# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
# Добавлена проверка директорий

import os
import random
import string

def generate_files_with_extensions(extension_counts, directory=None):
    if directory is not None:
        if not os.path.exists(directory):
            os.makedirs(directory)
        elif not os.path.isdir(directory):
            print(f"Ошибка: {directory} не является директорией")
            return

    for extension, num_files in extension_counts.items():
        create_files_with_extension(extension, num_files, directory)

def create_files_with_extension(extension, num_files, directory=None, min_name_length=6, max_name_length=30, min_file_size=256, max_file_size=4096):
    for _ in range(num_files):
        name_length = random.randint(min_name_length, max_name_length)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length)) + '.' + extension

        if directory is not None:
            file_path = os.path.join(directory, file_name)
        else:
            file_path = file_name

        if os.path.exists(file_path):
            print(f"Предупреждение: Файл {file_path} уже существует. Пропуск.")
            continue

        file_size = random.randint(min_file_size, max_file_size)
        random_bytes = os.urandom(file_size)

        with open(file_path, 'wb') as file:
            file.write(random_bytes)

# Example usage:
extension_counts = {
    'json': 10,
    'csv': 5,
    'pickle': 7,
}

generate_files_with_extensions(extension_counts, directory='output')

