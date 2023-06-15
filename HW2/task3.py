# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction


def calculate_fractions(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))

    fraction_sum = Fraction(numerator1, denominator1) + Fraction(numerator2, denominator2)
    fraction_product = Fraction(numerator1, denominator1) * Fraction(numerator2, denominator2)

    return fraction_sum, fraction_product


def calculate_fraction(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))

    # Вычислить общий знаменатель
    common_denominator = denominator1 * denominator2

    # Вычислить сумму дробей
    numerator_sum = numerator1 * denominator2 + numerator2 * denominator1
    fraction_sum = f"{numerator_sum}/{common_denominator}"

    # Вычислить произведение дробей
    numerator_product = numerator1 * numerator2
    fraction_product = f"{numerator_product}/{denominator1 * denominator2}"

    return fraction_sum, fraction_product


fraction1 = input("Введите первую дробь (в виде 'a/b'): ")
fraction2 = input("Введите вторую дробь (в виде 'a/b'): ")

sum_result, product_result = calculate_fraction(fraction1, fraction2)
print("Сумма: ", sum_result)
print("Произведение: ", product_result, end='\n')

print("Проверка:")
sum_result, product_result = calculate_fractions(fraction1, fraction2)
print("Сумма: ", sum_result)
print("Произведение: ", product_result)
