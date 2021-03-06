
#     ### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# Примеры:

# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

# duration = 400153

# h = duration // 3600
# m = (duration - h * 3600) // 60
# s = duration - (h * 3600 + m * 60)
# d = h // 24


# print(f'{d} дн {h} час {m} мин {s} сек')

# Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки работы кода сразу для нескольких значений
# продолжительности, будет ли тут полезен список?

# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

# res = [pow(i, 3) for i in range(100) if i % 2 != 0]
# my_sum = 0
# my_sum_list = []

# for i in range(len(res)):
#     my_str = str(res[i])
#     my_list = list(my_str)
#     for i in range(len(my_list)):
#         my_list[i] = int(my_list[i])
#     for i in range(len(my_list)):
#         my_sum = my_sum + my_list[i]
#     if my_sum % 7 == 0:
#         print(my_sum)
#         my_sum_list.append(my_sum)

# res = [pow(i, 3) + 17 for i in range(100) if i % 2 != 0]
# my_sum = 0
# my_sum_list = []

# for i in range(len(res)):
#     my_str = str(res[i])
#     my_list = list(my_str)
#     for i in range(len(my_list)):
#         my_list[i] = int(my_list[i])
#     for i in range(len(my_list)):
#         my_sum = my_sum + my_list[i]
#     if my_sum % 7 == 0:
#         print(my_sum)
#         my_sum_list.append(my_sum)

#     Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
#     К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#      Решить задачу под пунктом b, не создавая новый список.

# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание. Пробуйте их решать, если уверены в своих силах.

# n = 30

# for i in range(n + 1):
#     my_str=str(i + 1)
#     my_list = list(my_str)
#     if int(my_list[-1]) == 1 and i + 1 != 11:
#         print('{} процент'.format(i + 1))
#     elif int(my_list[-1]) > 1 and int(my_list[-1]) <= 4:
#         if  i + 1> 10 and i + 1<= 14:
#             print('{} процентов'.format(i + 1))
#         else:
#             print('{} процента'.format(i + 1))
#     else:
#         print('{} процентов'.format(i + 1))
