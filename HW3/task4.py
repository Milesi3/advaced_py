# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

def camping_vocabulary(friends):
    vocabulary = {}

    # Создание словаря
    for friend, things in friends.items():
        vocabulary[friend] = set(things)

    # Нахождение вещей, общих для всех друзей
    common_things = set.intersection(*vocabulary.values())

    # Поиск вещей, общих для всех друзей
    unique_things = {}
    for friend, things in vocabulary.items():
        unique_things[friend] = things - set.union(*(vocabulary[f] for f in vocabulary if f != friend))

    # Находит вещи, которые есть у всех, кроме одного друга
    one_friend_missing = {}
    for friend, things in vocabulary.items():
        others_things = set.union(*(vocabulary[f] for f in vocabulary if f != friend))
        one_friend_missing[friend] = others_things - things

    return common_things, unique_things, one_friend_missing



friends = {
    "Alice": ["палатка", "спальный мешок", "фонарик"],
    "Bob": ["палатка", "походная печь", "спальный мешок"],
    "Charlie": ["палатка", "спальный мешок", "туристические ботинки"]
}

common, unique, one_missing = camping_vocabulary(friends)

print("Обычные вещи:", common)
print("Уникальные вещи для каждого друга:", unique)
print("То, что есть у всех, кроме одного друга:")
for friend, things in one_missing.items():
    missing_friend = [f for f in one_missing if f != friend][0]
    print(f"{friend} отсутствует:", things)
    print("Выпадающий друг:", missing_friend)
    print()
