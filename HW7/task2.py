# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать в качестве аргумента желаемое конечное имя файлов.
# 2. При переименовании в конце имени добавляется порядковый номер.
# 3. принимать в качестве аргумента расширение исходного файла.
# 4. Переименование должно работать только для этих файлов внутри каталога.
# 5. принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>


import os


def rename_files_in_groups(new_name, original_extension, new_extension):
    directory = 'output'

    files = [file for file in os.listdir(directory) if file.endswith(original_extension)]

    for i, file in enumerate(files, start=1):
        original_name = os.path.splitext(file)[0]
        position = str(i).zfill(2)

        new_file_name = f"{original_name}_{new_name}_{position}.{new_extension}"

        old_file_path = os.path.join(directory, file)
        new_file_path = os.path.join(directory, new_file_name)

        os.rename(old_file_path, new_file_path)

        print(f"Renamed: {file} -> {new_file_name}")


rename_files_in_groups("new_name", ".txt", "csv")

