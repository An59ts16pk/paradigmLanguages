# Задача №1.
# Дан список целых чисел numbers. 
# Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания.
# Можно использовать любой алгоритм сортировки.

listNumbers1 = [4, 1, 9, 10, 2, 1, 5, 12, 0, 8]
# Сортировка пузырьком циклом for:
def sort_list_imperative(numbers):
    # Императивный код здесь
    lenList = len(numbers)
    for i in range(lenList-1):
        for j in range(lenList-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

print('\nImperative style solution:')
print(listNumbers1)
sort_list_imperative(listNumbers1)
print(listNumbers1)

# Задача №2.
# Написать точно такую же процедуру, но в декларативном стиле.

listNumbers2 = [4, 1, 9, 10, 2, 1, 5, 12, 0, 8]
# Сортировка встроенным метод в пайтон
def sort_list_declarative(numbers):
    # Декларативный код здесь
    numbers.sort(reverse=True)
    print(numbers)

print('\nDeclarative style solution:')
print(listNumbers2)
sort_list_declarative(listNumbers2)
