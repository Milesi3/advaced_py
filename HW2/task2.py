# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def decimal_to_hexadecimal(n):
    if n == 0:
        return '0'

    hex_digits = "0123456789ABCDEF"
    hex_string = ''

    while n > 0:
        remainder = n % 16
        hex_string = hex_digits[remainder] + hex_string
        n //= 16

    return hex_string



number = int(input("Введите число: "))
hexadecimal = decimal_to_hexadecimal(number)
print("Результат: ", hexadecimal)
print("Проверка: ",  hex(number)[2:])
