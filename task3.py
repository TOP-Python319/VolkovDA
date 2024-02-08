number_of_minutes= int(input("Введите количество минут: "))
Counting_the_hours = number_of_minutes// 60 #считаем часы
Counting_the_minutes = number_of_minutes % 60 #считаем оставшиеся минуты
print(f"{number_of_minutes} мин-это {Counting_the_hours} час {Counting_the_minutes} мин ")
