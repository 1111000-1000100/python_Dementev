# Дан целочисленный список размера 10. Вывести все содержащиеся в 
# данном списке чётные числа в порядке убывания их индексов, а также их количество K.

import random

# Создаем список размера 10 с случайными целыми числами
lst = [random.randint(1, 100) for _ in range(10)]
print("Исходный список:", lst)

# Фильтруем чётные числа и сортируем их по убыванию индексов
even_numbers = [num for num in lst if num % 2 == 0]
even_numbers_sorted = sorted(even_numbers, reverse=True)

# Выводим результат
print("Чётные числа в порядке убывания индексов:", even_numbers_sorted)
print("Количество чётных чисел (K):", len(even_numbers_sorted))