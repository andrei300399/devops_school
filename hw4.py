# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода ввиде строк (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:
#
# 1. После запуска предлагает пользователю ввести целые неотрицательные числа,
# разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).
# 2. Получив вводные данные, выделяет полученные числа, суммирует их,
# и печатает полученную сумму.
#
# Например:
#
# -> 12 12 12
# 36
#
# -> 123dfgdr%0&45ty-45--900
# -777

text = input("Введите строку:")
sum_numbers = 0
temp_text = ""
for i in range(len(text)):
    if text[i].isdigit():
        temp_text += text[i]
    elif temp_text == "":
        if text[i] == "-" and i + 1 < len(text) and text[i + 1].isdigit():
            temp_text += text[i]
        continue
    else:
        sum_numbers += int(temp_text)
        temp_text = ""

if temp_text:
    sum_numbers += int(temp_text)
print(sum_numbers)
