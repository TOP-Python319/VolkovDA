print("Программа должна получить от пользователя целую и дробную часть числа миль за два ввода")
dist1 = int(input("Введите первое число до запятой:"))
dist2 = int(input("Введите второе число после запятой:"))
num = dist1 + (dist2 / 10)
print(f"{num} миль = {(num*1.61):.1f} км")

# Внимательно читайте задание целиком, нужно было так же скопировать пример ввода и пример вывода, тем не менее в первый раз засчитываю. =)

# Пример ввода:
#     15
#     7

# Пример вывода:
#     15.7 миль = 25.3 км