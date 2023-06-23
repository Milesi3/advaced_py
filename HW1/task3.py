# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint
import sys

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10


def play_game(LOWER_LIMIT=0, UPPER_LIMIT=1000, MAX_ATTEMPTS=10):
    # Генерация случайного числа
    num = randint(LOWER_LIMIT, UPPER_LIMIT)

    print(f"Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT}. У вас есть {MAX_ATTEMPTS} попыток.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = int(input("Попытка {}: Ваше предположение: ".format(attempt)))

        if guess == num:
            print("Поздравляем! Вы угадали число {} за {} попыток.".format(num, attempt))
            return True
        elif guess < num:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

    print("К сожалению, вы не угадали число. Загаданное число было {}.".format(num))
    return False


if __name__ == "__main__":
    _, *parametr = sys.argv
    play_game(*map(int, parametr))
