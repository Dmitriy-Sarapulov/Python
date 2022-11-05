# Урок 3. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# Анониманые методы или Лямбда

# def f(x):
    # x**2
# g = f # если присвоить значениие функции в переменную, 
# то при вызове функции и вызове переменной(в которую присвоена функция) результат будет одинаковый. 
# print(type(f))
# print(type(g))

# def f(x): #Начальный вид функции
    # return x**2
# print(f(2))
# g = f #f - фуе=нкция g-переменная которая хранит в себе функцию. 
# print(type(f))
# print(type(g))
# print(f(4))
# print(g(4))

# функция с одной переменной

# def calc1(x):
#     return x+ 10
# # print(calc1(10))

# def calc2(x):
#     return x * 10
# # print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2,10) #вызов функции, с аргументом в виде функции.

# с двумя переменными:

# def sum(x, y):
#     return x + y

# def mult(x, y):
    # return x * y

# def calc(op, a, b): # функция которая в качестве аргумента принимает операцию, 
# а вкачестве операндов она принимает 2 аргумента. op - отдельная ф-я
    # print(op(a,b))
    # return(op(a,b))
# calc(mult, 4, 5)

#лямбда

#f = lambda q, w: q + w # описание одной строкой ф-ции sum.
# sum = lambda x, y: x + y # запись лямбда функции. 
# calc(sum,4,5) # при ее вызове получим тот же результат(9)
# Пропускаем шаг присвоения переменной и сокращаем код ещё на одну строку.
# calc(lambda x, y: x + y, 4 ,5) # Вызываем ф-ю calc c аргументами x, y и после : укказываем их значения.рез(9).

# list Comprehension - быстрое создание списков(условно)

# создаем некоторый список в диапазоне от 1 до 100

# list = [] # РАсписываем создание и заполнение листа как обычно
# for i in range(1, 101):
#     # if(i%2 == 0):
#         list.append(i)
# print(list)

# list = [i for i in range(1, 21)] #Это локоничная одностроковая запись того,что написано выше.
# # Взяты числа до 20 для упрщения чтения
# print(list)

# list = [i for i in range(1, 21) if i % 2 ==0] # добовляем условие внесения в список только четных чисел
# print(list)

# list = [(i, i) for i in range(1, 21) if i % 2 ==0] # подключаем кортежи, получаем на выходе пару чисел
# print(list)

# def f(x):
    # return x ** 3

# list = [(i, f(i)) for i in range(1, 21) if i % 2 ==0] # будет бежать по реджу, 
# потом выбирать только четные числа и после этого будет выполняться ф-я возведения чисел в 3-ю степень
# (число и его куб)
# print(list)

# from fileinput import close
# import re

# в файле хранятся числа нужно выбрать чётны и составить список пар(число; квадрат числа)
# пример: 1 2 3 4 8 15 23 38
# получить:
# [(2, 4), (8,64), (38, 1444)]

# path = '/Users/Admin/Desktop/Python/file.txt'
# f  = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = [] # создание пустого листа, который в дальнейшем будет заполняться.

# while data != '': # запускаю цикл с условием делать до тех пор пока моя строка не пустая.
#     space_pos = data.index(' ') # найти первую позицию пробела
#     numbers.append(int(data[:space_pos]))  # Взять все что находится в промежутке от первого символа 
#     # до позици первого пробела, превратить это в число и добавить в лист nubers(список номеров)
#     data = data[:space_pos + 1] # обновить строку с учетом уже обработанного,того что нам больше не надо.

# out = [] # создаем новый список.
# for e in numbers: # проегаемся по исходному списку nubers
#     if not e % 2: # проверка условия четности числа
#         out.append((e, e ** 2)) #добавляем в лист out пары числел (число, число в степени 2)
# print(out) # выводим список

#улучшение предыдущего кода
# def select(f, col): # создаем функцию, которая как аргумент принимает функцию и список данных
#     return[f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split() # с помощью split на выходе получим набор строк

# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x ** 2), res)
# print(res)

# функция map эта функция применяет указанную функцию к каждому элементу итерируемого объекта и 
# возвращает итератор с новыми объекатми(нельзя пройтись дважды)

# li = [x for x in range (1, 20)] #пример list Comprehension
# li = list(map(lambda x: x + 10, li)) # делаем грубое преобразование, чтоб получить список чисел
# print(li)

# data = list(map(int, input().split()))
# print(data)

# data = map(int, input().split())

# for e in data: print(e)

# функция filter применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор
# с теми объектами для которых функция вернула true.

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data)) # пример функции фильтр
# print(res)

# функция zip() применяется к набору итерируемых объектов и возвращает 
# итератор с кортежами из элементов входных данных
# (пробегается по минимальному списку элементовесли в первом арументе 5 значений,а во втором 3, 
# то смешает он только 3 значения первого с 3 значениями второго)

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids, salary))
# print(data)

# ф-я enumerate применяется к итерируемуму объекту и возвращает 
# новый итератор с кортежами из индекса и элементов входных данных.

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(enumerate(users))
# print(data)