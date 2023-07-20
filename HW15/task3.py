import argparse
import datetime
import logging

FORMAT = '{levelname} - {asctime}. ' \
         'Записал сообщение: {msg}'

logging.basicConfig(filename="log3", filemode='a', encoding="Utf-8", level=logging.ERROR, format=FORMAT, style="{")
logger = logging.getLogger(__name__)

MONTHS = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
}

DAYS = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}

def text_to_date(text):
    try:
        parts = text.split()
        day = int(parts[0].replace('-й', '').replace('-е', ''))

        if parts[1] in DAYS:
            weekday = DAYS[parts[1]]
        else:
            raise ValueError(f'Invalid weekday: {parts[1]}')

        if parts[2] in MONTHS:
            month = MONTHS[parts[2]]
        else:
            raise ValueError(f'Invalid month: {parts[2]}')

        year = datetime.datetime.now().year

        date = datetime.datetime(year, month, day)
        while date.weekday() != weekday:
            date += datetime.timedelta(days=1)

        return date
    except ValueError as e:
        logger.error(f"Ошибка {e}")
        return None

parser = argparse.ArgumentParser(description='Convert text to date')
parser.add_argument('--text', help='text to convert')
parser.add_argument('--day', help='day of the month (default: first day of the month)', default=1, type=int)
parser.add_argument('--weekday', help='weekday (default: current weekday)', choices=DAYS.keys())
parser.add_argument('--month', help='month (default: current month)', choices=MONTHS.keys())

args = parser.parse_args()

if args.text is not None:
    date = text_to_date(args.text)
else:
    year = datetime.datetime.now().year
    month = MONTHS[args.month] if args.month is not None else datetime.datetime.now().month
    day = args.day
    weekday = DAYS[args.weekday] if args.weekday is not None else datetime.datetime.now().weekday()

    date = datetime.datetime(year, month, day)
    while date.weekday() != weekday:
        date += datetime.timedelta(days=1)

print(date)




