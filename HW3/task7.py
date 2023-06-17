# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

def find_valid_option(things, max_capacity):
    # Сортировка вещей по массе в порядке возрастания
    sorted_things = sorted(things.items(), key=lambda x: x[1])

    current_capacity = 0
    backpack = []

    for item, mass in sorted_things:
        if current_capacity + mass <= max_capacity:
            backpack.append(item)
            current_capacity += mass

        if current_capacity == max_capacity:
            break

    return backpack

things_to_hike = {
    "Бутылка воды": 0.5,
    "Снэк": 0.3,
    "Карта": 0.2,
    "Аптечка": 0.7,
    "Камера": 1.2,
    "Дождевик": 0.8
}

max_capacity = 2.5

valid_option = find_valid_option(things_to_hike, max_capacity)
print("Подходящий вариант для рюкзака:", valid_option)

