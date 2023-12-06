# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную. 

import math
import numpy

# Вариант 1
def pearsonCorrelation_1(arr_x, arr_y):
    if len(arr_x) != len(arr_y):
        return "Ошибка! Массивы должны быть одинаковой длины"
    lenarr = len(arr_x)

    average_x = float(sum(arr_x) / lenarr)
    average_y = float(sum(arr_y) / lenarr)

    numerator = 0
    value_x = 0
    value_y = 0
    for i in range(lenarr):
        xdiff = arr_x[i] - average_x
        ydiff = arr_y[i] - average_y
        numerator += xdiff * ydiff
        value_x += xdiff ** 2
        value_y += ydiff ** 2

    return numerator / math.sqrt(value_x * value_y)

# Вариант 2
def pearsonCorrelation_2(arr_x, arr_y):
    if len(arr_x) != len(arr_y):
        return "Ошибка! Массивы должны быть одинаковой длины"
    lenarr = len(arr_x)

    average_x = float(sum(arr_x) / lenarr)
    average_y = float(sum(arr_y) / lenarr)

    value_x = sum([(xi - average_x) ** 2 for xi in arr_x]) 
    value_y = sum([(yi - average_y) ** 2 for yi in arr_y])
    numerator = sum([(xi - average_x) * (yi - average_y) for xi, yi in zip(arr_x, arr_y)])

    return numerator / (math.sqrt(value_x * value_y))

#array_1 = [1, 2, 3]
#array_2 = [1, 5, 7]
    
array_1 = numpy.random.randint(0, 9, 10)
array_2 = numpy.random.randint(0, 9, 10)

pCorr = pearsonCorrelation_2(array_1, array_2)
print(pCorr)