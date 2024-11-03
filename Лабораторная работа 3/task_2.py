def find_common_participants(str1, str2, n=','):
    str_1 = set(str1.split(n))
    str_2 = str2.split(n)
    common_participants = list(str_1.intersection(str_2))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, '|')
