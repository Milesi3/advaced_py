# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки

def display_words_with_line_numbers(text):
    words = text.split()
    words_sorted = sorted(words, key=lambda x: (x.encode('utf-8'), x))

    max_word_length = max(len(word) for word in words_sorted)
    line_number_width = len(str(len(words)))

    for i, word in enumerate(words_sorted, start=1):
        line_number = str(i).rjust(line_number_width)
        padding = ' ' * (max_word_length - len(word) + 1)
        print(f"{line_number} {padding}{word}")

article_text = input("Введите тест без знаков припинания: ")
print("Отсоритированый список")
display_words_with_line_numbers(article_text)
