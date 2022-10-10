# Урок 4. Данные, функции и модули в Python. Продолжение

# 30). Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)

# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# 31). Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 70 = 2*5*7 => [2, 5, 7]
# 140 = 2*2*5*7 => [2, 2, 5, 7]
# 140|2
# 70|2
# 35|5
# 7|7

# n = int(input("Введите число: "))
# i = 2 
# lst = []
# old_n = n
# while i <= n:
#     if n % i == 0:
#         lst.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old_n} приведены в списке: {lst}")

# 32). Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Введенные числа: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Неповторяющиеся элементы: {new_lst}")

# 33). Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x*2 + 4*x + 5 = 0
# или
# 2*x^2 + 4*x + 5 = 0

# import random

# k = int(input("Введите степень к: "))
# string = ''
# for i in range(k + 1):
#     a = random.randint (0,100)
#     if i < k and k-i != 1:
#         string = string + str(a) + '*x^' + str(k - i) + ' + '
#     elif k - i == 1:
#         string = string + str(a) + '*x' + ' + '
#     else:
#         string = string + str(a)
# string = string + ' = 0'
# print(string)
# data = open('file3.txt', 'a')
# data.write(string)
# data.close()

# 34). Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. 
# Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые).
# Пример:
# 1 Файл : 2*x2 + 4*x + 5 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0
# Пример:
# 1 Файл : 2*x3 + 4*x2 + 5*x + 1 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 2*x3 + 8*x2 + 12

# import random

# k = int(input("Введите степень к: "))

 


# def get_coef(k):
#     lst = []
#     for i in range(k + 1):
#         a = random.randint (0,100)
#         lst.append(a)        
#     return lst

# def get_mnogochlen (lst, name):
#     string = ''
#     a=len(lst)-1
#     for i in range(a+1): 
#         if i < a and a-i != 1:
#             string = string + str(lst[i]) + '*x^' + str(a - i) + ' + '
#         elif a - i == 1:
#             string = string + str(lst[i]) + '*x' + ' + '
#         else:
#             string = string + str(lst[i])
#     string = string + ' = 0'
#     data = open(name, 'a')
#     data.write(string + '\n')
#     data.close()    

# def sum_coef(list1, list2):
#     list3 = []
#     for i in range(len(list1)):
#         list3.append(list1[i] + list2[i])
#     return list3


# lst1=get_coef(k)
# get_mnogochlen (lst1, 'file4.txt')
# lst2=get_coef(k)
# get_mnogochlen (lst2, 'file5.txt')
# lst3=sum_coef(lst1, lst2)
# get_mnogochlen (lst3, 'file6.txt')