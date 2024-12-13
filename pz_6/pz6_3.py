# Дан список размера N. Заменить каждый элемент списка на среднее арифметическое этого элемента и его соседей. через random

import random

# Создаем список размера N с случайными целыми числами
try:
    while True:
        N = int(input("Введите размер списка: "))
        if N <= 0:
            print("Число не может быть меньше или равно нулю!")
            continue
        break

    lst = [random.randint(1, 100) for _ in range(N)]
    print("Исходный список:", lst)

    # Создаем новый список с замененными элементами
    new_lst = []

    for i in range(len(lst)):
        # Определяем соседей
        left = lst[i - 1] if i > 0 else lst[i]
        right = lst[i + 1] if i < len(lst) - 1 else lst[i]
    
        # Вычисляем среднее арифметическое
        average = (left + lst[i] + right) / 3
        new_lst.append(average)

    print("Список после замены элементов на среднее арифметическое:", new_lst)
except ValueError:
    print("Ошибка при вводе данных!")