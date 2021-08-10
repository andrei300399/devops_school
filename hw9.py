# Решить несколько задач из projecteuler.net
#
# Решения должны быть максимально лаконичными, и использовать list comprehensions.
#
# problem9 - list comprehension : one line
# problem6 - list comprehension : one line
# problem48 - list comprehension : one line
# problem40 - list comprehension

# problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
[[print(b*a*(1000-a-b)) for b in range(a + 1, 1000-(a*2)) if (a**2 + b**2 == (1000-a-b)**2)] for a in range(1, 333)]

#problem6 Sum square difference
[i*i for i in range(1, 101)]
