# 14). Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = list(input('Введите число: '))

def summa(number):

    sum = 0
    for i in number:    
        if i in ('0','1','2','3', '4', '5', '6', '7', '8', '9'):
            sum += int(i)
    return sum

print(f'сумма чисел равна: {summa(number)}')