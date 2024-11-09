try:
    A = int(input("Введите целое число A: "))
    B = int(input("Введите целое число B: "))
    if A % 2 != 0 and B % 2 != 0:
        print("Утверждение истино.")
    else:
        print("Утверждение ложно.")
except ValueError:
    print("Проверьте правильность ввода данных.")