def print_each_word(input_str):
    """
    Выводит в консоль каждое отдельное слово из строки
    (слова должны быть разделены символом ' ') с его
    последовательным номером (начиная с 1). Если длина
    слова превышает 10 символов, для решения задачи
    будут использоваться только первые 10 символов.

    :param input_str: строка, введенная пользователем
    :return:
    """

    words = input_str.split()
    words = [word if len(word) < 11 else word[:11] for word in words]
    for num, word in enumerate(words, start=1):
        print(f"{num}. {word}")