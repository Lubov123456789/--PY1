def get_count_char1(dict_) -> dict:
    # TODO вернуть словарь где частота символа заменена на процентное соотношение ко всем остальныm

    count1 = 0
    summa = sum([int(dict_.get(char)) for char in dict_])

    for char in dict_:
        dict_[char] = round(dict_[char] / summa * 100, 3)
        count1 += dict_[char]
    if round(count1) == 100:
        return dict_
    else:
        raise ValueError('Сумма процентных соотношений элементов словаря не равна 100')


def get_count_char(str_) -> dict:
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    chars = {}

    for char in str_:
        if char.isalpha() is True and char in chars:
            chars[char] += 1
        elif char.isalpha() is True:
            chars[char] = 1

    return chars


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(get_count_char1(get_count_char(main_str)))
