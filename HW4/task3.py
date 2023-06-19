# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Прошлое решение задачи лежит в HW2/task1

Start_Sum = 0
count = 0
history = []


def nalog(choice):
    global Start_Sum, count
    if Start_Sum >= 5000000:
        Start_Sum *= 0.9
        print('Вычли налог за богатство')
    if choice in ('1', '2') and count % 3 == 0:
        Start_Sum *= 1.03
        print('Третья операция, начисли 3 процента')
    return Start_Sum


def pop_sum(choice):
    Pop_Sum = int(input('Введите сумму пополнения кратную 50 у.е.: '))
    global Start_Sum, count
    if Pop_Sum % 50 == 0:
        Start_Sum += Pop_Sum
        print('Операция успешна')
        count += 1
        print(nalog(choice))
        return Pop_Sum
    else:
        print(f'Введеное число {Pop_Sum} не кртано 50 у.е.')
        return 'Ошибка операции'


def rent_sum(choice):
    Pop_Sum = int(input('Введите сумму снятие кратную 50 у.е.: '))
    global Start_Sum, count
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
        count += 1
        print(nalog(choice))
        return Pop_Sum
    else:
        print(f'Введеное число {Pop_Sum} не кртано 50 у.е.')
        return 'Ошибка операции'


def history_add(Pop_Sum, history, choice):
    if choice == '1':
        history.append(f"+{Pop_Sum}")
    if choice == '2':
        history.append(f"-{Pop_Sum}")


while True:
    choice = input('Выберите действие(1-пополнить, 2-снять, 3-выйти): ')

    match choice:
        case '1':
            Pop_Sum = pop_sum(choice)
            history_add(Pop_Sum, history, choice)
        case '2':
            Pop_Sum = rent_sum(choice)
            history_add(Pop_Sum, history, choice)
        case '3':
            print(nalog(choice))
            print(history)
            exit()
        case _:
            print('Действие не определенно')
            print(nalog(choice))
