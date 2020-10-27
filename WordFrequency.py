# функция для сортировки словаря и перевода его в список
def sort_dictionary_by_value(dictionary):
    list_of_sorted_pairs = [(k, dictionary[k])
                            for k in sorted(dictionary.keys(), key=dictionary.get, reverse=False)]
    # Так мы создаём кортежи (ключ, значение) из отсортированных элементов по ключу равному "значение ключа"
    # Также отсортированы будут и ключи, имеющие одно значение
    # "reverse = False" говорит, что перебор нужно делать в обычном порядке
    return list_of_sorted_pairs  # после сделанных операций возвращаем получившийся список


if __name__ == '__main__':
    words = input().lower().rsplit()  # Ввод строки с понижением регистра и раздилителем
    counter = {}
    dot = []
    max_len_word = 0
    underscore = 0
    for i in words:  # Цикл для нахождения максимальной дилны слова
        if len(i) > max_len_word:
            max_len_word = len(i)

    for word in words:  # Цикл для заполнения словаря значениями
        c = words.count(word)  # Переменная хранит в себе значение частоты встречаемости слова
        if c >= 10:
            c = 10
        if len(word) < max_len_word:  # Сравнение длины слова с максимальным значением
            underscore = max_len_word - len(word)
        elif len(word) == max_len_word:
            underscore = 0
        dot = [dot * c for dot in '.']  # Создание ключа в виде точек
        counter['_' * underscore + word] = dot  # Заполение словаря значениями слов с подчеркиваниями и записью ключей

    finally_list = sort_dictionary_by_value(counter)  # Сортируем полученный словарь
    for x in finally_list:  # Выводим на экран
        print(x[0], str(x[1]))

