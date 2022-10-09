# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

from functools import reduce

def sequence(number):
    list_of_products = [round((1+1/x)**x, 4) for x in range(1, number+1)]
    sum = reduce(lambda x, y: x + y, list_of_products)
    print(f"Сумма чисел = {round(sum, 4)}")
    return list_of_products


n = int(input('Введите число: '))
print(sequence(n))

