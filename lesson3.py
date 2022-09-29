# Урок 3. Данные, функции и модули в Python

# 19 Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел.

# from time import time

# (f"Введите число = {int(time() % 1 * 100)}")

# C =50
# A = 2
# B = 3
# x = 1
# m = 100

# list = []

# for i in range(C):
#     x = (A* x + B) % m 
#     list.append(x)
# print(list)

# import time  # Второй способ реализации псевдослучайных чисел


# def Random_Set(start = 0,end = 1):
#     seconds = time.time()
#     Next = True
#     while Next:
#         Rand = end * (seconds % 1)
#         if Rand >= start or Rand > end: Next = False
        
    
#     return int(Rand)

# print(Random_Set(1,1000))

# 20 Задайте список. Напишите программу, которая определит, присутствует ли в
# заданном списке строк некое число.

# n = int(input ( "Введите число: "))
# my_list = ["er567","iu5","rtu456t","ffg567" ]
# length = len(my_list)
# n = str(n)
# Flag = False
# for i in range (length):
#     if  my_list[i].find(n) != -1 :
#         Flag = True
#         break
# print (Flag)


# lst = ['efkdmfmlk445', 'jdfid 94i epr0 0i00ii4u8nfjdf', 'fglk38877 098 mekweir3m']
# num = int(input('Введите число для проверки: '))
# count = 0
# for elem in lst:
#     if str(num) in elem:
#         count += 1
# if count > 0:
#     print ('Да, присутствует')
# else:
#     print ('Не присутствует')

# 21 Напишите программу, которая определит позицию второго вхождения строки в
# списке либо сообщит, что её нет.

# def second_in(list, find):
#     count = 0
#     for i in range(len(list)):
#         if list[i] == find:
#             count += 1
#             if count == 2:
#                 return i
#     return -1


# list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# find = "йцу"

# print(second_in(list, find))
