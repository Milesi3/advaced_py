def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

def get_number():
    while True:
        number = input("Введите число (от 0 до 100000): ")
        if number.isdigit():
            number = int(number)
            if 0 <= number <= 100000:
                return number

        print("Пожалуйста, введите целое число от 0 до 100000.")
        print("Пожалуйста, введите целое число.")

number = get_number()
if is_prime(number):
    print("Число", number, "является простым.")
else:
    print("Число", number, "является составным.")