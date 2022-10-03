# Урок 3. Данные, функции и модули в Python

# 22. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# import random

# n = int(input('Введите кол-во элементов списка: '))
# ot = int(input('Введите диапазон от: '))
# do = int(input('Введите диапазон до: '))

# def generation_list(n, ot, do):
#     return [random.randint (ot,do) for i in range(n)]


# def sum_of_elements(list, n):
#     sum = 0
#     for i in range(0, n):
#         if i % 2 != 0:
#             sum += list[i]
#     return sum


# first_list = generation_list(n, ot, do)
# print(first_list)
# print(sum_of_elements(first_list, n))


# 23. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# import random

# n = int(input('Введите кол-во элементов списка: '))
# ot = int(input('Введите диапазон от: '))
# do = int(input('Введите диапазон до: '))

# def generation_list(n, ot, do):
#     return [random.randint (ot,do) for i in range(n)]

# def get_len(list):
#     len2 = 0
#     if len(list) % 2 == 0:
#         len2 = len(list) // 2
#     else:
#         len2 = len(list) // 2 + 1
#     return len2

# def multi_couple(list, len2):
#     second_list = []
#     for i in range(len2):
#         multi = list[i] * list[len(list)- i - 1]
#         second_list.append(multi)
#     return second_list
    

# first_list = generation_list(n, ot, do)
# len2 = get_len(first_list)
# print(first_list)
# print(multi_couple(first_list, len2))

# 24. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# import random

# n = int(input('Введите кол-во элементов списка: '))
# ot = int(input('Введите диапазон от: '))
# do = int(input('Введите диапазон до: '))

# def generation_list(n, ot, do):
#     return [round(random.uniform (ot,do), 2) for i in range(n)]

# def max_fract(list):
#     max = list[0] % 1
#     for i in list:
#         if i % 1 > max:
#             max = i % 1
#     return max

# def min_fract(list):
#     min = list[0] % 1
#     for i in list:
#         if i % 1 < min:
#             min = i % 1
#     return min

# first_list = generation_list(n, ot, do)
# print(first_list)
# print(round(max_fract(first_list) - min_fract(first_list), 2))

# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# n = int(input('Введите число: '))

# def convert_bin(n):
#     bin_number = bin(n)
#     return bin_number


# print(n)
# convert_number = convert_bin(n)
# string = str(convert_number)
# print(string.replace('0b',''))

# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# n = int(input('Введите число: '))

# def get_fibo_nums(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n + 1):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibo_nums(n)
# print(get_fibo_nums(n))
# print(fibo_nums.index(0))