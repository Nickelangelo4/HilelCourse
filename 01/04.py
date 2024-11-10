num1 = int(input("Введіть перше число: "))
operation = input("Введіть операцію (+, -, *, /): ")
num2 = int(input("Введіть друге число: "))


if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Помилка: ділення на нуль!"
else:
    result = "Невідома операція!"

print("Результат:", result)
