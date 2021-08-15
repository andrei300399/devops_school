#
# Напишите программу, которая читает данные из файлов
# /etc/passwd и /etc/group на вашей системе и выводит
# следующую информацию в файл output.txt:
# 1. Количество пользователей, использующих все имеющиеся
# интерпретаторы-оболочки.
# ( /bin/bash - 8 ; /bin/false - 11 ; ... )
# 2. Для всех групп в системе - UIDы пользователей
# состоящих в этих группах.
# ( root:1, sudo:1001,1002,1003, ...)
dict_shells = {}
dict_uids = {}

with open('passwd', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        passwd_list = line.split(':')
        if passwd_list[6] not in dict_shells:
            dict_shells[passwd_list[6]] = 0
        dict_shells[passwd_list[6]] += 1
        dict_uids[passwd_list[0]] = passwd_list[2]

with open('output.txt', 'w', encoding='utf-8') as file:
    for k, v in dict_shells.items():
        file.write(f"{k[:-1]} - {v}\n")
    file.write(f"\n\ngroups\n")

dict_groups = {}

with open('group', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        group_list = line.replace("\n", "").split(":")
        group_name = group_list[0]
        dict_groups[group_name] = [] if not group_name in dict_uids else [dict_uids[group_name]]
        dict_groups[group_name] += [dict_uids[user] for user in group_list[3].split(",") if user != ""]


with open('output.txt', 'a', encoding='utf-8') as file:
    for k, v in dict_groups.items():
        file.write(f"{k}:{v}\n")
