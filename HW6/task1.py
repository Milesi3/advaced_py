# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
import sys

__all__ = ['_is_leap_year']

def _is_leap_year(year):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)

def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        if 1 > year < 9999:
            return False
        if 1 > month < 12:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if _is_leap_year(year):
                if day > 29:
                    return False
            elif day > 28:
                return False
        if day < 1 or day > 31:
            return False
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    _, date = sys.argv
    print(date)
    if is_valid_date(date):
        print("Дата существует")
    else:
        print("Дата не существует")