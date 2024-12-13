# Дан список размера N. Найти количество участков, на которых его элементы монотонно возрастают.

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

    # Находим количество участков с монотонным возрастанием
    count = 0
    increasing = False

    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            if not increasing:
                count += 1
                increasing = True
        else:
            increasing = False

    print("Количество участков с монотонным возрастанием:", count)
except ValueError:
    print("Ошибка при вводе данных!")