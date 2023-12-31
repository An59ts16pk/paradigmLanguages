# Домашнее задание
# Таблица умножения
# ● Условие
#   На вход подается число n.
# ● Задача
#   Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
#   Обоснуйте выбор парадигм.
# ● Пример вывода
#   1 * 1 = 1
#   1 * 2 = 2
#   1 * 3 = 3
#   1 * 4 = 4
#   .........
#   1 * 9 = 9

print('\nТаблица умножения')
num = int(input("Введите число от 1 до 9: "))
print('\n')

for i in range(num, 10):
    for j in range(1, 10):
        print('{0} * {1} = {2}'.format(i, j, i*j))
    print('===========')

# Это структурное программирование
# используется вложенный цикл for и нет оператора GOTO
# Выбор сделан в эту парадигму, потому что здесь нет необходимости
# переиспользовать код, да и в других программах вряд ли понадобиться
# выводить на экран таблицу умножения, разве только в учебных, да и 
# при использлвании процедуры или функции не дало бы выигрыша по 
# количеству строк кода 