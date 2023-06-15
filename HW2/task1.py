# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

Start_Sum = 0
count = 0

def nalog(Start_Sum, choice, count):
    if Start_Sum >= 5000000:
        Start_Sum *= 0.9
        print('Вычли налог за богатство')
    if choice in ('1', '2') and count % 3 == 0:
        Start_Sum *= 1.03
        print('Третья операция, начисли 3 процента')
    return Start_Sum


while True:
    choice = input('Выберите действие(1-пополнить, 2-снять, 3-выйти): ')

    match choice:
        case '1':
            Pop_Sum = int(input('Введите сумму пополнения кратную 50 у.е.: '))
            if Pop_Sum % 50 == 0:
                Start_Sum += Pop_Sum
                print('Операция успешна')
            else:
                print(f'Введеное число {Pop_Sum} не кртано 50 у.е.')
            count += 1
            print(nalog(Start_Sum, choice, count))
        case '2':
            Pop_Sum = int(input('Введите сумму снятие кратную 50 у.е.: '))
            if Start_Sum >= Pop_Sum and Pop_Sum % 50 == 0:
                Start_Sum -= Pop_Sum
                print('Операция успешна')
                kom = Pop_Sum * 0.015
                if kom < 30:
                    Start_Sum -= 30
                    print('Коммисия за снятие 30')
                elif 30 <= kom <= 600:
                    Start_Sum -= kom
                    print(f'Коммисия за снятие {kom}')
                else:
                    Start_Sum -= 600
                    print('Коммисия за снятие 600')
            else:
                print(f'Введеное число {Pop_Sum} не кртано 50 у.е.')
            count += 1
            print(nalog(Start_Sum, choice, count))
        case '3':
            print(nalog(Start_Sum, choice, count))
            exit()
        case _:
            print('Действие не определенно')
            print(nalog(Start_Sum, choice, count))
