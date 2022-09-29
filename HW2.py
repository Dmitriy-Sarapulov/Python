# 14). Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# number = list(input('Введите число: '))

# def summa(number):

#     sum = 0
#     for i in number:    
#         if i in ('0','1','2','3', '4', '5', '6', '7', '8', '9'):
#             sum += int(i)
#     return sum

# print(f'сумма чисел равна: {summa(number)}')

# 15). Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input('Введите число N: '))
# multiplication = 1
# for i in range(n):
#     multiplication = multiplication * (i + 1)
#     print(multiplication)

# 16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.

# n = int(input('Введите число: '))
# sum = 0

# for i in range(1, n + 1):
#     count = (1+1/i)**i
#     sum += count
# print(sum)


# 17). Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции 
# (случайные) хранятся в файле file.txt 
# (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.

# from random import randint

# n = int(input('Введите число: '))


# def position_generation(n):
#     data = open('file2.txt', 'a')
#     for i in range(3):
#         a=randint(0, 2 * n + 1)
#         b = str(a)+'\n'
#         data.write(b)
#     data.close()


# def generation_list(n):
#     list = []
#     for i in range(-n, n+1):
#         list.append(i)
#     return list

# def get_positions(path):
#     data = open(path, 'r')
#     dlist = [int(line.strip()) for line in data]
#     data.close()
#     return dlist
    

# def multi(list, dlist):
#     multiplication = 1
#     for i in dlist:
#         multiplication *= list[i]
#     return multiplication


# path = 'file2.txt'
# position_generation(n)
# list2 = generation_list(n)
# dlist2 = get_positions(path)
# result = multi(list2, dlist2)
# print(list2)
# print(result)

# 18). Реализуйте алгоритм перемешивания списка.

# import random

# def generation_list(n, ot, do):
#     return [random.randint (ot,do) for i in range(n)]

# def shake_nums(list):
#     return random.shuffle(list)

# n = int(input('Введите количество элементов: '))
# ot = int(input('Введите диапазон от: '))
# do = int(input('Введите диапазон до: '))

# list1 = generation_list(n, ot, do)
# print(list1)
# shake_nums(list1)
# print(list1)



