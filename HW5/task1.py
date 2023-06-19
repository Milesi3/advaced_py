# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def input_text(text):
    array_text = text.split("\\")
    name_file = array_text[-1].split('.')
    result = {text, name_file[0], name_file[1]}
    return tuple(result)


text = input("Введите путь к файлу: ")
print(input_text(text))

# мб как то проще можно
