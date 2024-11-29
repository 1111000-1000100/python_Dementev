#Начальный вклад в банке равен 1000 руб. Через каждый месяц размер вклада
#увеличивается на P процентов от имеющейся суммы (P — вещественное число, 0< P
#<25). По данному P определить, через сколько месяцев размер вклада превысит 1100
#руб., и вывести найденное количество месяцев K (целое число) и итоговый размер
#вклада S (вещественное число).

def calculate_deposit(P):

    initial_deposit = 1000
    target_deposit = 1100
    
    if not (0 < P < 25):
        raise ValueError("Процентная ставка должна быть в пределах от 0 до 25")
    
    monthly_rate = P / 100
    
    current_deposit = initial_deposit
    month_count = 0
    
    while current_deposit <= target_deposit:

        current_deposit *= (1 + monthly_rate)
        month_count += 1
    
    return month_count, round(current_deposit, 2)


while True:
    try:
        P = float(input("Введите процентную ставку (от 0 до 25): "))
        months, final_deposit = calculate_deposit(P)
        print(f"Через {months} месяцев размер вклада составит {final_deposit} рублей.")
        break
    except ValueError:
        print("Неверно введена процентная ставка. Попробуйте еще раз.")