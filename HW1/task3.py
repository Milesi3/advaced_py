from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

def play_game():
    # Генерация случайного числа
    num = randint(LOWER_LIMIT, UPPER_LIMIT)

    print("Угадайте число от 0 до 1000. У вас есть 10 попыток.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = int(input("Попытка {}: Ваше предположение: ".format(attempt)))

        if guess == num:
            print("Поздравляем! Вы угадали число {} за {} попыток.".format(num, attempt))
            break
        elif guess < num:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

    print("К сожалению, вы не угадали число. Загаданное число было {}.".format(num))

play_game()
