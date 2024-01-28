# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите кол-во монеток: '))
count_eagles = 0
count_tailes = 0

for i in range(n):
    coin = int(input('Если орел введите 1, если решка 0 '))
    if coin == 1:
        count_eagles += 1
    elif coin == 0:
        count_tailes += 1
if count_eagles > count_tailes:
    print(f'Надо перевернуть {count_tailes} монеток')
else:
    print(f'Надо перевернуть {count_eagles} монеток')