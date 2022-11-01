from itertools import count
from functools import reduce
# # Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# # Объект типа Генератор: 

# def check_even_1(numbers): # Обычный метод
#     even = [] # который создает и заполняет массив(список)
#     for num in numbers:
#         if num % 2 == 0:
#             even.append(num*num)
#     return even # в Результате, заполенный список он хранит в памяти.

# def check_even_3(numbers): # Это объект типа генератор не создает и не хранит массив
#     for num in numbers:
#         if num % 2 == 0:
#             yield num * num # yield вернуть объект генератора. Мы не храним ничего в памяти,а делаем по запросу.

# #Если не нужно обращаться к объекту по индексу, то можно использовать генератор.

# # Если сравнивать по скорости и кол-ву задействованной памяти функцию list comprehension 
# # и ф-цию filter, то фильтр будет эффективней.

# def check_even_1(lst): # ф-ция с использованием LC 
#     new_list = [i for i in lst if i % 2 == 0] # пример записи LC
#     return new_list
# # тут мы будем хранить список
# def check_even_2(lst): # ф-ция с использованием filter и lambda
#     new_list = filter(lambda x: x % 2 == 0, lst) # пример записи filter и lambda
#     return new_list
# # тут мы будем хранить объект ф-цуу фильтр.

# # Исключения try except:

# try:  # ТОчка где выполняется выражение
#     res = 100/0
# except ZeroDivisionError:  # отлов ошибки + генерация исключения(заявленного: ZeroDivisionError)
# # можно сделать общее(Exception)
#     print('На ноль делить нельзя')
# else:  # Если except не сработал.
#     print(f"Все хорошо, результат - {res}")
# finally:  # Срабатывает всегда
#     print("Программа завершена")

# # класс-это исключение,исключение-это класс
# # Создать класс исключение от класса Exception
# # Сгенерировать исклчение в нужной точке программы
# # Отловить и обработать

# class OwnError(Exception): #создаем класс исключения(OwnError), он наследует от класса (Exception) 
# # мы написали условия исключения
#     def __init__(self, txt): #генерация исключения
#         self.txt = txt

# inp_data = input("Введите положительное число: ")

# try:
#     inp_data = int(inp_data)
#     if inp_data < 0:
#         raise OwnError("ВЫ ввели отрицательное число!") #rise генерация исключения(поднятие исключения)
# except OwnError as err:
#     print(err)
# else:
#     print(f"Все хорошо, Ваше Число: {inp_data}")

# LC пименение.
# вывести только те элементы массива, который больше предыдущих.
# lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# lst = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]] # использовать только в случачае 
# когда условий не много и это читаемо

# print(lst)

# # дан разбег 20-240, необходимо найти числа кратные 20 и 21

# lst = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
# print(lst)

# # достать элементы у которых нет повторений:
# lst = [300, 300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# lst = [el for el in lst if lst.count(el) == 1]
# print(lst)

# #Факториал числа пример: 4! = 1*2*3*4 рассчёт через генератор.
# # ф-я count в пределах чего(с чего начинать, старт)
# def fact(n):
#     factorial = 1
#     for x in count(1):
#         if x > n:
#             break
#         factorial = factorial * x
#         yield factorial #вернет ОБЪЕКТ ГЕНЕРАТОРА

# n = int(input("Введите число: "))
# i = 0
# for el in fact(n): #считает все до n
#     i += 1
#     print(f"!{i} = {el}")

# # range это от и до, count это с чего то
# # ф-я reduce(импортируется) 

# lst = [x for x in range(100, 1001, 2)]
# res = reduce(lambda item, item2: item * item2, lst) #применение лямбда ф-ии к элементам массива сводя все к 1 значению
# print(res)

# аргумеентом у reduce может быть любая ф-ия
