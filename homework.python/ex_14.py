# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число '))

i = 0
k = 2**i

while k <= n:
    print(k)
    i += 1
    k = 2**i