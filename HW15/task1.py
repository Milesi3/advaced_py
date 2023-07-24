import logging

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created}   {msg}'

logging.basicConfig(format=FORMAT, style="{", filename="log", filemode='a', encoding="Utf-8", level=logging.ERROR)
logger = logging.getLogger()


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.error("Деление на 0")


division(2, 0)
