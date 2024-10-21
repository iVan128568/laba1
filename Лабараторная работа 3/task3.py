
def letters(str_):
    arr = []
    str_ = str_.lower()
    for i in str_:
        if i.isalpha() and i not in arr:
            arr.append(i)
    return arr


# TODO  Напишите функцию count_letters
def count_letters(str_):
    return {i:(str_.count(i) + str_.count(i.upper())) for i in letters(str_)}



# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_, len_):
    return {i:(dict_[i] / len_) for i in list(dict_.keys())}


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
def get_formated(dict_):
    for key, value in dict_.items():
        value = round(res_dict[key], 2)
        value = str(value).ljust(4, '0')
        yield key, value


res_dict = count_letters(main_str)
res_dict = calculate_frequency(res_dict, len([i for i in main_str if i.isalpha()]))
for key, value in get_formated(res_dict):
    print(f"{key}: {value}")


