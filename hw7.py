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
with open('/etc/passwd', 'r', encoding='utf-8') as file:
    dict_shells = {}
    for line in file.readlines():
        if  line.split(':')[6] not in dict_shells:
            dict_shells[line.split(':')[6]] = 0;
        dict_shells[line.split(':')[6]] +=1;
    print(dict_shells)




