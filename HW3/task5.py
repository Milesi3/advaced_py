# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def remove_duplicates(input_list):
    return list(set(input_list))

original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
result_list = remove_duplicates(original_list)
print("Вводимый список:", original_list)
print("Список без дубликатов:", result_list)
