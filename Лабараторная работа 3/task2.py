# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, sep = ','):
    playas1, playas2 = [set(str.split(sep)) for str in (str1, str2)]
    return sorted(playas1 & playas2)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))