#  https://projecteuler.net/problem=36
#
# The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2. (Please note that the palindromic number,
# in either base, may not include leading zeros.)
#
# Напишите программу, которая решает описанную выше задачу и печатает ответ.
def is_palindromic(number):
    return number == number[::-1]


sum_palindromic = 0

for i in range(1000000):
    if is_palindromic(str(i)) and is_palindromic(str(bin(i))[2:]):
        sum_palindromic += i

print(sum_palindromic)
