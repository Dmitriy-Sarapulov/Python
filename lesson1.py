#Знакомство с языком пайтон, семинар

#print('hello мир')
#0. Вывести квадрат числа
#number = int(input('Введите число '))
#print('Квадрат числа {} Равен {}'.format(number, number**2))
#print(f'Квадрат числа {number} Равен {number**2}')
#print('Квадрат числа {} Равен {}'.format(number, number**2))

# проверить, является ли одно число квадратом другого

#a = input(input("A="))
#b = input(input("B="))

# Программа которая принимает 5 чисел и ищет максимальное из них

#list = [1, 8, 3, 6, 5]
#max = list[0]
#for i in list:
    #if max < i:
       # max = i
#print(f'Максимальное число равно {max}')

#Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#a = abs(int(input('N = ')))
#for i in range(-a,a+1): # Вывод от х до -х
#    print(i,end=' ')

#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#a=float(input('Введите дробное число число: '))
#n=int(a*10%10)
#print(n)

#5.	Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

#a=int(input('A='))
#if ((a%5 == 0 and a%10 == 0) or a%15 == 0)and a % 30 != 0:
#    print('кратно 5 и 10 или 15, но не 30')

#x V y вывести значения. V- or /\ - and  не1 - not(1)
#print('x y z f')
#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            f = x or y or z
#            print(x, y, z, bool(f))