# Надо написать функцию которая возвращает N-мерный массив с ширинами заданными в аргументе списком из N элементов:
# n_arr([2,2])
# >> [[“”,“”],[“”,“”]]
# n_arr([2,2,2])
# >> [[[“”,“”],[“”,“”]], [[“”,“”],[“”,“”]]]
from copy import deepcopy


def n_arr(lst):
    if len(lst) < 2:
        return [""] * lst.pop()
    else:
        last = lst.pop()
        sub_arr = n_arr(lst)
        return [deepcopy(sub_arr) for i in range(last)]


arr = (n_arr([4, 2, 3]))

print(arr)
