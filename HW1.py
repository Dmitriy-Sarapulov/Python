#Домашняя работа 1
#Задача 6
#Напишите программу, которая принимает на вход цифру, обозначающую день
#недели, и проверяет, является ли этот день выходным.

#day = int(input('Введите номер дня недели: '))
#if day <= 0 or day > 7:
#    print('Введены неверные данные ')
#elif day >= 1 and day < 6:
#    print('Этот день не является выходным ')
#else :
#    print('Этот день является выходным ')

# задача 8
#Напишите программу, которая принимает на вход координаты точки (X и Y),
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта
#точка (или на какой оси она находится).

# x = int(input('Введите координату х: '))
# y = int(input('Введите координату y: '))

# def quarter_definition(x, y):
#     if x == 0 and y == 0:
#        print('Центр координат')
#     elif x > 0 and y > 0:
#        print('Первая четверь')
#     elif x > 0 and y < 0:
#        print('Вторая четверь')
#     elif x < 0 and y < 0:
#        print('третья четверь')
#     elif x < 0 and y > 0:
#        print('Четвертая четверь')
#     elif x == 0 and y != 0:
#        print(f'Лежит на оси у, y = {y} ')
#     elif x != 0 and y == 0:
#        print(f'Лежит на оси x, x = {x} ')
#     else:
#        print('Невозможно определить четверть')
#     return (x, y)

# quarter_definition(x, y)
 
# Задача 9

#qart = int(input('Введите номер четверти: '))

# def range_definition(qart):
#    if qart == 4:
#        print('х(0;-∞), y(0;+∞)')
#    elif qart == 1:
#        print('х(0;+∞), y(0;+∞)')
#    elif qart == 2:
#        print('х(0;+∞), y(0;-∞)')
#    elif qart == 3:
#        print('х(0;-∞), y(0;-∞)')
#    else:
#        print('Введены неверные данные')

#range_definition(qart)

# Задача 10 Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

# x1 = int(input('Введите координаты х1: '))
# y1 = int(input('Введите координаты y1: '))
# x2 = int(input('Введите координаты х2: '))
# y2 = int(input('Введите координаты y2: '))

# distance = round(((x2 - x1)**2 + (y2 - y1)**2)**(0.5),2)
# print(f'Длина отрезка: {distance}')

# задача 7
# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# print('x y z f1   f2')
# for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            f1 = not(x or y or z)
#            f2 = (not x) and (not y) and (not z) 
#            print(x, y, z, bool(f1), bool(f2))