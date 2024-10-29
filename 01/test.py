
number = int(input("Введіть 4-значне число: "))

user_number1 = number // 1_000
user_number2 = (number % 1_000) // 1_00
user_number3 = (number %1_00) // 10
user_number4 = number % 10

print(user_number1)
print(user_number2)
print(user_number3)
print(user_number4)