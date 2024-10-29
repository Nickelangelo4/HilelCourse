number = int(input("Введіть 5-значне число: "))

user_number1 = number % 10
user_number2 = (number // 10) % 10
user_number3 = (number // 1_00) % 10
user_number4 = (number // 1_000) % 10
user_number5 = number // 10_000

reversed_number = (user_number1 * 10_000) + (user_number2 * 1_000) + (user_number3 * 1_00) + (user_number4 * 10) + user_number5

print("Перевернене число: ", reversed_number)