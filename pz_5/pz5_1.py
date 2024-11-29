#Составить программу, в которой функцию построит изображение, в котором в
#первой строке 1 звездочка, во второй - 2, в третьей -3, ..., в строке с номером m - m
#звездочек.

def draw_stars(m):
    for i in range(1, m+1):
        print('*' * i)

while True:
    try:
        m = int(input("Введите число строк: "))
        if m < 0:
            print("Число не может быть отрицательным!")
            continue
        break
    except ValueError:
        print("Ошибка при вводе числа!")
        continue
draw_stars(m)