# Написать функцию Фиббоначи fib(n), которая вычисляет
# элементы последовательности Фиббоначи:
# 1 1 2 3 5 8 13 21 34 55 .......
import math


def fib(n):
    # Формула Бине
    return math.floor(((((1 + 5 ** (1 / 2)) / 2) ** n) - (((1 - 5 ** (1 / 2)) / 2) ** n)) / (5 ** (1 / 2)))


print(fib(9))


def fib2(n):
    # цикл
    n1 = n2 = 1
    if n < 3:
        return 1
    for i in range(3, n + 1):
        n1, n2 = n2, n2 + n1
    return n2


print(fib2(8))
