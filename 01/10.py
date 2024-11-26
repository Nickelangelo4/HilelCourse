print("Вітаємо у калькуляторі!")

while True:
    try:
        num1 = float(input("Введіть перше число: "))
        operation = input("Введіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Ділення на нуль неможливе!")
                continue
        else:
            print("Невірна операція. Спробуйте ще раз.")
            continue

        print(f"Результат: {result}")
    except ValueError:
        print("Введено некоректне число. Спробуйте ще раз.")
        continue

    cont = input("Бажаєте продовжити? (y/yes для продовження): ").strip().lower()
    if cont not in ('y', 'yes'):
        print("Дякуємо за використання калькулятора! До побачення!")
        break