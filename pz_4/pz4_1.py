#Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A
#до B включительно.

while True:
    try:
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))
        
        if A >= B:
            print("Ошибка! Число A должно быть меньше B.")
            continue
        if A < 0 or B < 0:
            print("Ошибка! Числа должны быть положительными!")
            continue

        break
    except ValueError:
        print("Пожалуйста, введите целое число!")

sum_of_squares = 0

for i in range(A, B + 1):
    sum_of_squares += i ** 2

print(f"Сумма квадратов всех целых чисел от {A} до {B} равна {sum_of_squares}")