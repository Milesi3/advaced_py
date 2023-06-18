# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хэшируем, используйте его строковое представление.

def create_dictionary(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not isinstance(value, (int, float, str)):
            value = repr(value)
        if not isinstance(key, (int, float, str)):
            key = str(key)
        result[value] = key
    return result


dictionary = create_dictionary(arg1="value1", arg2="value2", arg3=[1, 2, 3])
print(dictionary)

# Не понял сути здания, но вроде работает
