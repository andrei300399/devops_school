# Написать функцию-генератор, которая объединяет два отсортированных итератора.
# Результирующий итератор должен содержать последовательность в которой содержаться все элементы из каждой коллекции, в упорядоченном виде.
#
# list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]
it1 = iter([2, 2, 2, 2])
it2 = (x for x in range(2, 6))


def merge(iterator1, iterator2):
    first, second = next(iterator1), next(iterator2)
    try:
        while True:
            if first is None:
                try:
                    first = next(iterator1)
                except StopIteration:
                    yield second
                    second = next(iterator2)
                    continue

            if second is None:
                try:
                    second = next(iterator2)
                except StopIteration:
                    yield first
                    first = next(iterator1)
                    continue
            if first < second:
                yield first
                first = None
            else:
                yield second
                second = None

    except:
        return


print(list(merge(it1, it2)))
