# Гипотеза Коллатца
# может быть кратко выражена следующим образом:
#
# берём любое натуральное число n, если оно чётное,
# то делим его на 2 если нечётное, то умножаем на 3
# и прибавляем 1 (получаем 3n + 1) над полученным
# числом выполняем те же самые действия, и так далее.
#
# Гипотеза Коллатца заключается в том, что какое бы
# начальное число n мы ни взяли, рано или поздно мы
# получим единицу.
#
# Пример
# Для числа 12:
# 12
# 6
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# Всего получаем 9 шагов.
#
# Задача
# Вычислить число шагов для числа n, согласно гипотезе
# Коллатца необходимых для достижения этим числом единицы.
def get_count_steps(n):
    count_steps = 0
    while n != 1:
        if n % 2:
            n = (3 * n + 1)
        else:
            n /= 2
        count_steps += 1
    return count_steps


print(f"12: count steps {get_count_steps(12)}")
print(f"1: count steps {get_count_steps(1)}")
print(f"5: count steps {get_count_steps(5)}")
print(f"10: count steps {get_count_steps(7)}")
